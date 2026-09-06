"""
Copia las figuras de cada caso a `src/content/cases/<slug>/images/`.

Los nombres no coinciden a los dos lados y no deben coincidir: en el repositorio
del caso están en español (`03_vender_es_estructural.png`) y en el sitio en
inglés (`03-selling-is-structural.png`), porque todo lo publicado va en inglés.
Lo que sí coincide, y es lo que hace posible copiarlas sin una tabla que
mantener, es el **prefijo numérico**: las figuras se numeran en el mismo orden en
los dos sitios.

Por eso el script empareja por ese prefijo y **aborta antes de copiar nada** si la
correspondencia no es exacta: si un lado tiene una figura de más, si un prefijo
se repite o si falta. Copiar una figura sobre la que no le toca es el error caro
aquí — nadie lo nota hasta que un gráfico ilustra el hallazgo equivocado.

Uso:
    python scripts/cases/sync_figures.py
"""

import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SITIO = AQUI.parents[1]
ESPACIO = AQUI.parents[2]

CASOS = ESPACIO / 'cases'
CONTENIDO = SITIO / 'src' / 'content' / 'cases'

SLUGS = [
    'steam-price-reception',
    'football-transfer-market',
    'sba-loan-vintages',
]


def por_prefijo(carpeta):
    """{'01': Path(...), '02': ...} para los PNG numerados de una carpeta."""
    indice = {}
    for png in sorted(carpeta.glob('*.png')):
        m = re.match(r'(\d+)', png.name)
        if not m:
            continue
        if m.group(1) in indice:
            raise SystemExit(f'Prefijo {m.group(1)} repetido en {carpeta}')
        indice[m.group(1)] = png
    return indice


def main():
    if not CASOS.is_dir():
        print(f'No encuentro {CASOS}: este script necesita el espacio de trabajo completo.')
        return 1

    planes = []
    for slug in SLUGS:
        origen = por_prefijo(CASOS / slug / 'salidas' / 'graficos')
        destino = por_prefijo(CONTENIDO / slug / 'images')

        if origen.keys() != destino.keys():
            print(f'{slug}: los prefijos no coinciden.')
            print(f'  caso:  {sorted(origen)}')
            print(f'  sitio: {sorted(destino)}')
            return 1

        planes.append((slug, origen, destino))

    # Nada se copia hasta que los tres casos han cuadrado.
    for slug, origen, destino in planes:
        print(f'{slug}')
        for prefijo in sorted(origen):
            shutil.copyfile(origen[prefijo], destino[prefijo])
            print(f'  {origen[prefijo].name}  ->  {destino[prefijo].name}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
