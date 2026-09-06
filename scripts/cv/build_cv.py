"""
Genera `public/cv.pdf` a partir de `cv.html`.

El contenido del CV se edita en `cv.html`; aquí solo se resuelve lo que el
navegador no puede resolver por su cuenta y se imprime.

Dos cosas que no son obvias:

1. El HTML se abre como `file://`, así que las rutas absolutas del sitio
   (`/fonts/...`) no llevan a ninguna parte. Las fuentes se incrustan en base64
   antes de imprimir, igual que `reporte.py` hace con las figuras de los casos:
   lo que se le pasa a Chrome es un archivo autocontenido.

2. La detección del navegador replica el patrón de
   `case-template/notebooks/reporte.py` — construir los candidatos desde las
   variables de entorno, nunca incrustar `C:\\Program Files\\...` en el código.
   Se replica y no se importa: `reporte.py` vive en otro repositorio y su API es
   la de un reporte de caso, no la de un CV. Copiar el motor entero solo
   crearía una segunda copia que diverge.

Uso:
    python scripts/cv/build_cv.py
"""

import base64
import os
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SITIO = AQUI.parents[1]

FUENTE = AQUI / 'cv.html'
RENDER = AQUI / 'cv.render.html'          # temporal, ignorado por git
SALIDA = SITIO / 'public' / 'cv.pdf'

# (familia CSS, archivo en public/fonts, rango de pesos de la fuente variable)
FUENTES = [
    ('Inter', 'inter-latin-var.woff2', '400 700'),
    ('Fraunces', 'fraunces-latin-var.woff2', '400 700'),
]

MARCADOR = '/* FUENTES */'


def navegador():
    """Chrome o Edge, buscado sin incrustar una sola ruta absoluta."""
    sufijos = [
        r'Google\Chrome\Application\chrome.exe',
        r'Microsoft\Edge\Application\msedge.exe',
    ]
    bases = [os.environ.get(v) for v in ('ProgramFiles', 'ProgramFiles(x86)', 'LOCALAPPDATA')]

    for base in filter(None, bases):
        for sufijo in sufijos:
            ruta = Path(base) / sufijo
            if ruta.exists():
                return str(ruta)

    for nombre in ('google-chrome', 'chromium', 'chromium-browser', 'chrome'):
        ruta = shutil.which(nombre)
        if ruta:
            return ruta

    return None


def con_fuentes(html):
    """Sustituye el marcador de `cv.html` por los @font-face en base64."""
    bloques = []
    for familia, archivo, pesos in FUENTES:
        datos = (SITIO / 'public' / 'fonts' / archivo).read_bytes()
        b64 = base64.b64encode(datos).decode('ascii')
        bloques.append(
            f"@font-face {{\n"
            f"  font-family: '{familia}';\n"
            f"  src: url(data:font/woff2;base64,{b64}) format('woff2');\n"
            f"  font-weight: {pesos};\n"
            f"  font-style: normal;\n"
            f"}}"
        )

    if MARCADOR not in html:
        raise SystemExit(f'Falta el marcador {MARCADOR} en {FUENTE.name}.')

    return html.replace(MARCADOR, '\n'.join(bloques))


def main():
    html = con_fuentes(FUENTE.read_text(encoding='utf-8'))
    RENDER.write_text(html, encoding='utf-8')

    chrome = navegador()
    if chrome is None:
        print(f'HTML escrito en {RENDER.relative_to(SITIO)}')
        print('Sin Chrome ni Edge: el PDF se obtiene abriendo ese archivo e imprimiendo a PDF.')
        return 1

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            chrome,
            '--headless',
            '--disable-gpu',
            # Sin la URL y la fecha que el navegador imprime en los márgenes: no
            # aportan nada al lector y ensucian lo que extrae un ATS.
            '--no-pdf-header-footer',
            f'--print-to-pdf={SALIDA}',
            RENDER.as_uri(),
        ],
        check=True,
        capture_output=True,
        timeout=180,
    )

    print(f'{SALIDA.relative_to(SITIO)} — {SALIDA.stat().st_size / 1024:.0f} KB')
    return 0


if __name__ == '__main__':
    sys.exit(main())
