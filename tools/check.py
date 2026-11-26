#!/usr/bin/env python3
"""Prüf-Agent: testet training/show.html + content.json. Exit 0 = ok, 1 = Fehler.
Aufruf: python3 tools/check.py [--shots ordner]"""
import json, subprocess, sys, time, os, re, threading, http.server, socketserver
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
shots = None
if '--shots' in sys.argv:
    shots = Path(sys.argv[sys.argv.index('--shots')+1]); shots.mkdir(parents=True, exist_ok=True)
errs, warns = [], []

# 1) content.json
try:
    c = json.load(open(ROOT/'training/content.json', encoding='utf-8'))
except Exception as e:
    print('FEHLER content.json ungültig:', e); sys.exit(1)
for k in '0123456':
    if not c.get('motto', {}).get(k): errs.append(f'motto[{k}] fehlt')
    al = c.get('mottoAlt', {}).get(k, [])
    for t in [c['motto'].get(k, '')] + al:
        if len(t) > 60: errs.append(f'Spruch zu lang ({len(t)}): {t[:40]}…')
if len(c.get('fakten', [])) < 20: errs.append('weniger als 20 Fakten')
for f in c.get('fakten', []):
    if len(f) > 150: errs.append(f'Fakt zu lang ({len(f)}): {f[:40]}…')
for a in c.get('aktionen', []):
    if not a.get('title') or len(a['title']) > 70: errs.append(f'Aktion Titel fehlt/zu lang: {a}')
    if len(a.get('text', '')) > 200: errs.append('Aktion Text zu lang')
    for k in ('von', 'bis'):
        if a.get(k) and not re.fullmatch(r'\d{4}-\d\d-\d\d', a[k]): errs.append(f'Aktion {k} Format: {a[k]}')

# 2) Browser
from playwright.sync_api import sync_playwright
os.chdir(ROOT)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), Q); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{port}/training/show.html'
days = ['11-19','11-25','11-28','11-29','12-01','12-06','12-14','12-24','12-31','01-05']
with sync_playwright() as p:
    b = p.chromium.launch()
    for day in days:
        for tv in (False, True):
            ctx = b.new_context(viewport={'width':1920,'height':1080},
                user_agent='Mozilla/5.0 (Linux; Android 9; AFTMM Build/PS7233) Silk/100 like Chrome/100 Safari/537.36' if tv else None)
            pg = ctx.new_page(); logs = []
            # Google Fonts sind für den Check irrelevant (Fallback-Schrift); in gesperrten Netzen nicht als Fehler werten
            pg.route(re.compile(r'https://fonts\.(googleapis|gstatic)\.com/.*'), lambda r: r.fulfill(status=200, content_type='text/css', body=''))
            # Wetter-Abruf (open-meteo) ebenfalls abfangen: der Check soll nicht vom Netz der Umgebung abhängen
            pg.route(re.compile(r'https://api\.open-meteo\.com/.*'), lambda r: r.fulfill(status=200, content_type='application/json', body='{"current":{"weather_code":3,"cloud_cover":50,"wind_speed_10m":5,"is_day":1}}'))
            pg.on('pageerror', lambda e: logs.append(str(e)))
            pg.on('console', lambda m: m.type == 'error' and logs.append(m.text))
            try:
                pg.goto(f'{base}?sday={day}&hold=1&manual=1', wait_until='load')
                pg.wait_for_timeout(600)
                n = pg.evaluate("document.querySelectorAll('.slide').length")
                if n < 8: errs.append(f'{day}{" TV" if tv else ""}: nur {n} Folien')
                # jede Folie: Text darf nicht aus der Bühne laufen
                bad = pg.evaluate("""()=>{const o=[];document.querySelectorAll('.slide').forEach((s,i)=>{s.classList.add('on');s.querySelectorAll('h1,h2,h3,p,li').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&(r.right>1925||r.bottom>1085))o.push((s.id||('#'+i))+': '+(e.textContent||'').slice(0,40))});s.classList.remove('on')});return o}""")
                for x in bad[:3]: errs.append(f'{day}{" TV" if tv else ""}: Text ragt raus – {x}')
                if shots and not tv and day in ('11-19','11-29','12-06','12-24'):
                    pg.screenshot(path=str(shots/f'{day}.png'))
            except Exception as e:
                errs.append(f'{day}: {e}')
            for l in logs:
                if 'content.json' not in l and 'favicon' not in l: errs.append(f'{day}{" TV" if tv else ""} JS-Fehler: {l[:120]}')
            ctx.close()
    b.close()
srv.shutdown()
errs = list(dict.fromkeys(errs))
for w in warns: print('Hinweis:', w)
if errs:
    print('FEHLER:'); [print(' -', e) for e in errs]; sys.exit(1)
print('OK: content.json gültig, 8 Testtage x (PC+TV) ohne Fehler')
