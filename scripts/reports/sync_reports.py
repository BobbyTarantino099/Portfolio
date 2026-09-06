"""
Copia los reportes técnicos de los casos a `public/reports/`.

Cada caso genera `entregables/reporte-tecnico.pdf` en su propio repositorio. El
sitio los sirve desde su dominio, así que hay que traerlos — y traerlos con un
script, no a mano, por la misma razón que el resto de binarios del proyecto: un
archivo copiado a mano deja de coincidir con su origen sin que nadie se entere.

Además del copiado, imprime el número de páginas y el tamaño de cada uno. Esos
son los datos que van al front-matter del caso (`report.pages`), y salen de
medir el archivo, no de recordarlo.

`site/` es un repositorio independiente: quien lo clone solo no tendrá al lado
la carpeta `cases/`. En ese caso el script lo dice y no hace nada — los PDF ya
copiados siguen versionados aquí y el sitio construye igual.

Uso:
    python scripts/reports/sync_reports.py
"""

import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SITIO = AQUI.parents[1]
ESPACIO = AQUI.parents[2]

CASOS = ESPACIO / 'cases'
DESTINO = SITIO / 'public' / 'reports'

SLUGS = [
    'steam-price-reception',
    'football-transfer-market',
    'sba-loan-vintages',
]


def paginas(pdf):
    """Cuenta los objetos de página del PDF, sin dependencias externas."""
    return len(re.findall(rb'/Type\s*/Page[^s]', pdf.read_bytes()))


def main():
    if not CASOS.is_dir():
        print(f'No encuentro {CASOS}.')
        print('Este script solo corre en el espacio de trabajo completo, con `cases/`')
        print('junto a `site/`. Los PDF ya copiados siguen en public/reports/.')
        return 1

    DESTINO.mkdir(parents=True, exist_ok=True)

    faltan = []
    for slug in SLUGS:
        origen = CASOS / slug / 'entregables' / 'reporte-tecnico.pdf'
        if not origen.is_file():
            faltan.append(slug)
            print(f'{slug}: falta {origen.relative_to(ESPACIO)} — genéralo con build_reporte.py')
            continue

        destino = DESTINO / f'{slug}.pdf'
        shutil.copyfile(origen, destino)
        print(f'{slug}.pdf — {paginas(destino)} páginas, {destino.stat().st_size / 1024:.0f} KB')

    return 1 if faltan else 0


if __name__ == '__main__':
    sys.exit(main())
