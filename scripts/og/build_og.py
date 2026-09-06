"""
Genera las tarjetas de enlace (`og:image`) en `public/og/`.

Una general para la home y las páginas sueltas, y una por caso con su propio
titular. Cuando alguien comparte un caso en LinkedIn, la tarjeta muestra el
hallazgo de ese caso y no un genérico.

Los titulares NO se escriben aquí: se leen del front-matter de cada caso, que es
la fuente única. Duplicarlos en este script sería el mismo error que el contrato
de contenido existe para evitar — el titular del sitio y el de la tarjeta
separándose sin que nadie se entere.

Mismo motor que el CV y los reportes: HTML autocontenido —fuentes y figura en
base64, porque se abre como `file://`— capturado con Chrome headless a 1200×630,
que es la proporción 1.91:1 que LinkedIn recorta sin tocar.

Uso:
    python scripts/og/build_og.py
"""

import base64
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SITIO = AQUI.parents[1]

CASOS = SITIO / 'src' / 'content' / 'cases'
FUENTES = SITIO / 'public' / 'fonts'
DESTINO = SITIO / 'public' / 'og'

ANCHO, ALTO = 1200, 630

# Los mismos tokens del sitio (src/styles/global.css), en su versión clara: una
# tarjeta se ve sobre el fondo de LinkedIn, no sobre el tema del lector.
PAPEL = '#fbfaf7'
TINTA = '#1a1815'
TINTA_SUAVE = '#5a564c'
REGLA = '#ddd9cf'
ACENTO = '#1f5fa8'


def navegador():
    sufijos = [
        r'Google\Chrome\Application\chrome.exe',
        r'Microsoft\Edge\Application\msedge.exe',
    ]
    for base in filter(None, (os.environ.get(v) for v in
                              ('ProgramFiles', 'ProgramFiles(x86)', 'LOCALAPPDATA'))):
        for sufijo in sufijos:
            ruta = Path(base) / sufijo
            if ruta.exists():
                return str(ruta)
    for nombre in ('google-chrome', 'chromium', 'chromium-browser', 'chrome'):
        ruta = shutil.which(nombre)
        if ruta:
            return ruta
    return None


def b64(ruta, mime):
    return f'data:{mime};base64,' + base64.b64encode(ruta.read_bytes()).decode('ascii')


def fuentes_css():
    bloques = []
    for familia, archivo in (('Inter', 'inter-latin-var.woff2'),
                             ('Fraunces', 'fraunces-latin-var.woff2')):
        datos = b64(FUENTES / archivo, 'font/woff2')
        bloques.append(
            f"@font-face {{ font-family: '{familia}'; src: url({datos}) format('woff2');"
            f" font-weight: 400 700; font-style: normal; }}"
        )
    return '\n'.join(bloques)


def front_matter(md):
    """Las cuatro claves que la tarjeta necesita. Sin PyYAML: es un bloque plano."""
    texto = md.read_text(encoding='utf-8')
    bloque = texto.split('---', 2)[1]
    datos = {}
    for clave in ('title', 'summary', 'hero', 'domain', 'scale'):
        m = re.search(rf'^{clave}:\s*"(.*)"\s*$', bloque, re.M)
        if m:
            datos[clave] = m.group(1)
    faltan = {'title', 'hero', 'domain', 'scale'} - datos.keys()
    if faltan:
        raise SystemExit(f'{md}: faltan claves en el front-matter: {sorted(faltan)}')
    return datos


ESTILO = f"""
{{FUENTES}}

* {{ box-sizing: border-box; margin: 0; }}

body {{
  width: {ANCHO}px;
  height: {ALTO}px;
  display: flex;
  overflow: hidden;
  background: {PAPEL};
  color: {TINTA};
  font-family: 'Inter', system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}}

.texto {{
  flex: 0 0 58%;
  padding: 54px 46px 46px 60px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

.eyebrow {{
  font-size: 17px;
  font-weight: 600;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: {ACENTO};
}}

h1 {{
  font-family: 'Fraunces', Georgia, serif;
  font-optical-sizing: auto;
  font-weight: 600;
  font-size: 52px;
  line-height: 1.08;
  letter-spacing: -0.02em;
  text-wrap: balance;
  margin-top: 22px;
}}

.tagline {{ font-size: 58px; }}

.pie {{ display: flex; align-items: center; gap: 14px; }}

.mono {{
  display: inline-grid;
  place-items: center;
  width: 46px;
  height: 46px;
  flex: none;
  background: {TINTA};
  color: {PAPEL};
  border-radius: 5px;
  font-family: 'Fraunces', Georgia, serif;
  font-weight: 600;
  font-size: 28px;
  line-height: 1;
  padding-top: 2px;
}}

/* Ni el nombre ni la escala envuelven: partidos en dos líneas el pie deja de
   leerse como una firma y empieza a parecer un párrafo. Si no cabe, encoge la
   escala, que es el dato prescindible de los dos. */
.nombre {{
  font-family: 'Fraunces', Georgia, serif;
  font-weight: 600;
  font-size: 22px;
  white-space: nowrap;
}}
.rol {{ font-size: 13px; letter-spacing: 0.13em; text-transform: uppercase; color: {TINTA_SUAVE}; }}
.escala {{
  margin-left: auto;
  padding-left: 18px;
  font-size: 15px;
  color: {TINTA_SUAVE};
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
}}

/* La figura entera, encuadrada, no recortada: recortarla dejaba su propio
   titular partido a media palabra en el borde, que es peor que no enseñarla.
   Entera se lee como lo que es —una lámina de análisis— aunque a tamaño de feed
   nadie descifre los ejes; el peso de la comunicación lo lleva el titular. */
.figura {{
  flex: 1;
  border-left: 1px solid {REGLA};
  background: #ffffff;
  overflow: hidden;
  display: grid;
  place-items: center;
  padding: 26px 22px;
}}

.figura img {{
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}}
"""


def html_caso(datos, figura_b64, fuentes):
    # Un titular largo a 52px se come el aire del pie. El salto es de un punto y
    # solo para los que lo necesitan: los cortos no tienen por qué encoger.
    tamano = 44 if len(datos['title']) > 78 else 52
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{ESTILO.replace('{FUENTES}', fuentes)}
h1 {{ font-size: {tamano}px; }}
</style></head><body>
  <div class="texto">
    <div>
      <p class="eyebrow">{datos['domain']}</p>
      <h1>{datos['title']}</h1>
    </div>
    <div class="pie">
      <span class="mono">J</span>
      <span>
        <span class="nombre">Juan Esteban Arenas</span><br>
        <span class="rol">Data analyst</span>
      </span>
      <span class="escala">{datos['scale']}</span>
    </div>
  </div>
  <div class="figura"><img src="{figura_b64}" alt=""></div>
</body></html>"""


def html_general(fuentes):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{ESTILO.replace('{FUENTES}', fuentes)}
.texto {{ flex: 1; padding: 64px 60px 52px; }}
</style></head><body>
  <div class="texto">
    <div>
      <p class="eyebrow">Data analysis case studies</p>
      <h1 class="tagline">Turning business questions into defensible recommendations.</h1>
    </div>
    <div class="pie">
      <span class="mono">J</span>
      <span>
        <span class="nombre">Juan Esteban Arenas</span><br>
        <span class="rol">Data analyst</span>
      </span>
      <span class="escala">Three published cases<br>SQL · Python · Power BI</span>
    </div>
  </div>
</body></html>"""


def capturar(chrome, html, destino):
    temporal = DESTINO / (destino.stem + '.render.html')
    temporal.write_text(html, encoding='utf-8')
    subprocess.run(
        [chrome, '--headless', '--disable-gpu', '--hide-scrollbars',
         f'--window-size={ANCHO},{ALTO}', '--virtual-time-budget=8000',
         f'--screenshot={destino}', temporal.resolve().as_uri()],
        check=True, capture_output=True, timeout=180,
    )
    temporal.unlink()
    print(f'  og/{destino.name} — {destino.stat().st_size / 1024:.0f} KB')


def main():
    chrome = navegador()
    if chrome is None:
        raise SystemExit('Sin Chrome ni Edge: no se pueden generar las tarjetas.')

    DESTINO.mkdir(parents=True, exist_ok=True)
    fuentes = fuentes_css()

    print('tarjetas:')
    capturar(chrome, html_general(fuentes), DESTINO / 'default.png')

    for md in sorted(CASOS.glob('*/index.md')):
        slug = md.parent.name
        datos = front_matter(md)
        # `hero` es relativo al propio index.md: "./images/03-....png"
        figura = (md.parent / datos['hero']).resolve()
        if not figura.is_file():
            raise SystemExit(f'{slug}: no encuentro la figura {figura}')
        capturar(chrome, html_caso(datos, b64(figura, 'image/png'), fuentes),
                 DESTINO / f'{slug}.png')

    return 0


if __name__ == '__main__':
    sys.exit(main())
