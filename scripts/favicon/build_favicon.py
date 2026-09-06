"""
Genera `public/favicon.svg`: la J del monograma sobre la caja de acento.

El favicon NO puede pedir la fuente. Un `<text font-family="Fraunces">` dentro de
un SVG se dibuja con la serif por defecto del navegador de quien visita, que no
es Fraunces y no se parece — el favicon acabaría siendo una letra ajena a la
marca. Así que el glifo se convierte a trazado aquí, a partir del mismo
`fraunces-latin-var.woff2` que sirve el sitio, y el SVG resultante no depende de
nada externo.

Fraunces es variable: se instancia en el peso 600 (el del monograma) y en el eje
óptico que corresponde a un tamaño pequeño, antes de sacar el contorno.

Uso:
    python scripts/favicon/build_favicon.py
"""

import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

AQUI = Path(__file__).resolve().parent
SITIO = AQUI.parents[1]

FUENTE = SITIO / 'public' / 'fonts' / 'fraunces-latin-var.woff2'
SALIDA = SITIO / 'public' / 'favicon.svg'

LETRA = 'J'
PESO = 600
# El eje óptico de Fraunces: 9 es el extremo de texto pequeño, donde los remates
# engordan y las astas se separan. Es lo que hace legible una letra a 16 px.
OPTICO = 9

LIENZO = 32
RADIO = 7
FONDO = '#1f5fa8'   # el azul de --accent, el mismo de los enlaces y las figuras
TINTA = '#ffffff'

# Proporción de la caja que ocupa la altura de mayúscula. Medido a ojo sobre el
# monograma del sitio: la letra ocupa algo más de la mitad del cuadro.
ALTURA_CAJA = 0.56


def main():
    fuente = TTFont(str(FUENTE))
    ejes = {a.axisTag for a in fuente['fvar'].axes} if 'fvar' in fuente else set()

    fijar = {}
    if 'wght' in ejes:
        fijar['wght'] = PESO
    if 'opsz' in ejes:
        fijar['opsz'] = OPTICO
    if fijar:
        fuente = instancer.instantiateVariableFont(fuente, fijar)

    glifos = fuente.getGlyphSet()
    nombre = fuente.getBestCmap()[ord(LETRA)]

    pluma = SVGPathPen(glifos)
    glifos[nombre].draw(pluma)
    trazado = pluma.getCommands()

    upm = fuente['head'].unitsPerEm
    altura_mayuscula = fuente['OS/2'].sCapHeight if hasattr(fuente['OS/2'], 'sCapHeight') else upm * 0.7
    ancho = glifos[nombre].width

    # Escala para que la altura de mayúscula ocupe ALTURA_CAJA del lienzo, y
    # traslación para centrar la letra ópticamente (la J de Fraunces no es
    # simétrica, así que se centra por su caja de tinta, no por su avance).
    escala = LIENZO * ALTURA_CAJA / altura_mayuscula
    x = (LIENZO - ancho * escala) / 2
    y = (LIENZO + altura_mayuscula * escala) / 2

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LIENZO} {LIENZO}">\n'
        f'  <rect width="{LIENZO}" height="{LIENZO}" rx="{RADIO}" fill="{FONDO}"/>\n'
        f'  <path transform="translate({x:.3f} {y:.3f}) scale({escala:.5f} -{escala:.5f})"\n'
        f'        fill="{TINTA}" d="{trazado}"/>\n'
        f'</svg>\n'
    )
    SALIDA.write_text(svg, encoding='utf-8')
    print(f'{SALIDA.relative_to(SITIO)} — {len(svg)} bytes, glifo {nombre} a peso {PESO}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
