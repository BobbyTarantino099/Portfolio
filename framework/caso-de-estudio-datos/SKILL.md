---
name: caso-de-estudio-datos
description: Ejecuta un caso de estudio de análisis de datos de principio a fin con las seis fases del proceso de análisis (Preguntar, Preparar, Procesar, Analizar, Compartir, Actuar), con puertas de calidad y entregables verificables en cada una, más anexos operativos de SQL, hojas de cálculo, Python/pandas y visualización. Usa esta skill siempre que aparezca un caso de estudio, un proyecto de portafolio de datos, un dataset nuevo que hay que convertir en conclusiones, una pregunta de negocio que responder con datos, la duda de qué caso de estudio hacer o qué dataset usar, o una petición de limpiar, analizar, visualizar, presentar o publicar datos — aunque la persona no nombre el framework ni pida explícitamente "un caso de estudio".
---

# Caso de estudio de análisis de datos

Framework operativo para llevar una pregunta de negocio hasta una recomendación defendible, con
evidencia y trazabilidad. Está basado en el proceso de análisis de datos de Google (Ask, Prepare,
Process, Analyze, Share, Act) y adaptado para producir **casos de estudio de portafolio**, no solo
análisis internos.

## Cuándo usarla

Úsala cuando exista una pregunta de negocio y datos (o la necesidad de conseguirlos). Aplica igual
si el caso es real, ficticio o de práctica.

**No la uses** para tareas de una sola pieza sin contexto de negocio: escribir una consulta SQL
aislada, explicar una función, depurar un script. En esos casos responde directo.

Si la persona todavía no tiene tema ni datos, empieza por `references/eleccion-del-caso.md` (fase 0)
antes de la fase 1.

## Reglas de operación

1. **Las fases son secuenciales y cada una tiene una puerta de salida.** No avances a la siguiente
   sin cumplir la checklist de salida del archivo de referencia correspondiente. Si algo falla,
   retrocede: descubrir en Analizar que los datos no responden la pregunta significa volver a
   Preguntar o Preparar, no improvisar.
2. **Todo se documenta mientras ocurre, no al final.** La documentación *es* el entregable en tres
   de las seis fases. Reconstruir de memoria produce casos de estudio flojos y ese es exactamente
   el detalle que un reclutador nota.
3. **Nada de datos inventados.** Si un número no salió de los datos, no entra al informe. Si hay
   una brecha, se declara como limitación.
4. **El artefacto vivo es `CASO.md`.** Se crea en la fase 1 y se actualiza al cerrar cada fase.
   Es lo que permite retomar el trabajo en otra sesión sin perder contexto.

## Flujo

| # | Fase | Pregunta que responde | Entregable | Referencia |
|---|------|----------------------|------------|------------|
| 0 | Elegir | ¿Vale la pena este caso? | Ficha de decisión del caso | `references/eleccion-del-caso.md` |
| 1 | Preguntar | ¿Cuál es el problema real y de quién? | Enunciado de la tarea de negocio | `references/01-preguntar.md` |
| 2 | Preparar | ¿Estos datos sirven y puedo confiar en ellos? | Descripción de todas las fuentes | `references/02-preparar.md` |
| 3 | Procesar | ¿Están limpios y puedo demostrarlo? | Bitácora de limpieza | `references/03-procesar.md` |
| 4 | Analizar | ¿Qué dicen los datos? | Resumen del análisis | `references/04-analizar.md` |
| 5 | Compartir | ¿Cómo lo entiende la audiencia? | Visualizaciones y hallazgos clave | `references/05-compartir.md` |
| 6 | Actuar | ¿Qué debería hacer el negocio? | Recomendaciones priorizadas | `references/06-actuar.md` |
| 7 | Portafolio | ¿Qué demuestra frente a los demás casos? | Página de caso publicada según el contrato, y presentación ensayada | `references/portafolio.md` |

La fase 0 se salta si la persona ya llega con tema y datos. La fase 7 ocurre una vez por caso, pero
sus decisiones (qué demuestra este caso) conviene tenerlas claras desde la fase 0.

## Cómo trabajar cada fase

Repite este ciclo por fase, una a la vez:

1. **Lee el archivo de referencia de la fase.** Contiene el detalle operativo, los marcos mentales
   aplicables y los errores comunes. No trabajes de memoria.
2. **Si la fase es Procesar o Analizar, lee también el anexo de la herramienta elegida** (`anexo-sql.md`,
   `anexo-hojas-de-calculo.md` o `anexo-python.md`). Si la fase es Compartir, lee
   `anexo-visualizacion.md`. Los anexos tienen su propia puerta de salida, que se suma a la de la fase.
3. **Ejecuta las tareas** de esa fase.
4. **Escribe el entregable** en `CASO.md` (plantillas en `references/plantillas.md`).
5. **Valida la puerta de salida** punto por punto. Enuncia en voz alta qué se cumplió y qué no.
6. **Confirma con la persona antes de avanzar.** Presenta el entregable y las decisiones que
   tomaste. Las decisiones de negocio y de alcance son suyas, no tuyas.

Antes de cerrar el caso completo, revisa `references/criterios-de-calidad.md`.

## Divulgación progresiva

**Carga solo lo que la fase actual necesita.** Cargar los doce archivos de referencia de golpe
degrada la calidad de las respuestas y desperdicia contexto. El orden correcto es: SKILL.md siempre
→ el archivo de la fase actual → el anexo de la herramienta si aplica → las plantillas cuando toca
escribir el entregable. `glosario.md` solo se consulta ante un término concreto.

## Estructura de archivos recomendada

El framework se instala **una sola vez** al nivel del portafolio, como hermano de las carpetas de
cada caso — no dentro de cada caso. Cada caso vive en su propia carpeta, con estructura idéntica
para que abrir cualquiera se sienta igual:

```
portafolio/                            # raíz del espacio de trabajo
├── framework/
│   └── caso-de-estudio-datos/         # esta skill, compartida por todos los casos
│       ├── SKILL.md
│       ├── references/
│       └── assets/
│
├── site/                              # el sitio del portafolio  [repositorio propio]
│   └── ...                            # publica L1 y L2 de cada caso
│
└── cases/
    ├── nombre-del-caso-1/             # [repositorio propio]
    │   ├── CASO.md                    # artefacto vivo: las 7 fases documentadas
    │   ├── README.md                  # abstract + cómo reproducir + enlace al sitio
    │   ├── bitacora-limpieza.md       # entregable de fase 3
    │   ├── documentacion/
    │   │   ├── fichas-de-fuente.md    # entregable de fase 2 (una ficha por fuente)
    │   │   └── diccionario-de-datos.md
    │   ├── datos/
    │   │   ├── crudos/                # SOLO LECTURA. Nunca se edita. Nunca se sube si es sensible.
    │   │   ├── intermedios/
    │   │   └── limpios/
    │   ├── notebooks/  o  consultas/  # scripts reproducibles
    │   ├── salidas/
    │   │   ├── graficos/              # las figuras que cruzan al sitio
    │   │   └── tablas/                # los agregados que cruzan al sitio
    │   └── entregables/               # resumen ejecutivo, presentación, fichas de recomendación
    │
    └── nombre-del-caso-2/
        └── ... (misma estructura)
```

Un repositorio por caso, más uno para el sitio. Así cada caso es navegable por sí solo —que es
donde miran los reclutadores técnicos— y el sitio no carga con notebooks ni datos.

Reglas duras:

- **Los datos crudos jamás se modifican in situ.** Toda transformación produce un archivo nuevo y
  queda registrada en la bitácora.
- **Nombre de archivo del crudo:** `origen_tema_periodo_version.csv` (convención de la fase 2),
  guardado dentro de `datos/crudos/`. No se deja además una copia suelta en la raíz del caso — es la
  fuente más frecuente de desorden y de confusión sobre cuál archivo es "el bueno".
- **`documentacion/` agrupa los entregables narrativos de fase 2** (fichas de fuente, diccionario de
  datos). Si el caso genera además un diario de datos, también va aquí.
- **`entregables/` agrupa lo que se entrega a la audiencia del caso**, no a la del portafolio:
  resumen ejecutivo, mazo de presentación, fichas de recomendación completas.
- **Nada de rutas absolutas en el código.** Toda ruta se resuelve desde la ubicación del propio
  script (`Path(__file__).resolve().parents[1]` en Python, `path.resolve(__dirname, '..')` en
  Node); toda imagen en un Markdown es relativa. Una ruta absoluta convierte un análisis
  reproducible en uno que solo corría en la máquina donde se escribió, y no se nota hasta que
  alguien clona el repositorio para comprobar tu trabajo.
- **Los datos pesados no se versionan.** Crudos y derivados van al `.gitignore` y se regeneran con
  los scripts. Lo que sí se versiona son las salidas: figuras y tablas agregadas.
- **El framework no se duplica por caso.** Si aparece una segunda copia dentro de la carpeta de un
  caso, es un error, no una variante: bórrala y deja solo la de `framework/`.

**El traspaso al sitio.** Al cerrar la fase 6, el caso entrega un Markdown con front-matter (la
plantilla 7 de `plantillas.md`) más sus figuras y sus tablas agregadas. Solo eso cruza al sitio;
`CASO.md`, los datos y los notebooks se quedan en el repositorio del caso y se enlazan. El contrato
completo está en `references/portafolio.md`, sección 2.

## Antipatrones que arruinan un caso de estudio

- **Empezar por el dataset.** Si eliges los datos antes que la pregunta, terminas respondiendo lo
  que los datos permiten en vez de lo que el negocio necesita.
- **Saltar de Preparar a Compartir.** Un gráfico bonito sobre datos sucios es un error con buena
  tipografía.
- **Confundir hallazgo con recomendación.** "Los usuarios casuales viajan más los fines de semana"
  es un hallazgo. "Lanzar la campaña de conversión el jueves, en estaciones de ocio" es una
  recomendación. La fase 6 exige lo segundo.
- **Omitir limitaciones.** Declararlas transmite criterio; ocultarlas destruye credibilidad en
  cuanto alguien pregunte.
- **Documentar al final.** Ver regla 2.

## Referencias

**Proceso** — se leen en orden, una por fase:

- `references/eleccion-del-caso.md` — fase 0: elegir tema, calibrar alcance, catálogo de datasets.
- `references/01-preguntar.md` … `references/06-actuar.md` — detalle operativo por fase.
- `references/portafolio.md` — fase 7: estrategia del conjunto, presentación, búsqueda de empleo.

**Anexos por herramienta** — se leen junto a la fase correspondiente:

- `references/anexo-sql.md` — estilo, JOINs, agregación, CTEs, rutina de exploración. Fases 3 y 4.
- `references/anexo-hojas-de-calculo.md` — errores y arreglos, funciones, tablas dinámicas. Fases 3 y 4.
- `references/anexo-python.md` — pandas de punta a punta, estructura del notebook. Fases 3, 4 y 5.
- `references/anexo-visualizacion.md` — selector de gráfico, diseño, accesibilidad, Tableau. Fase 5.

**Apoyo** — se consultan cuando hacen falta:

- `references/plantillas.md` — 13 plantillas copiables (CASO.md, bitácora, ficha de fuente, ficha de
  recomendación, **página de caso para el sitio**, guion de presentación, hoja de ruta, SOW, diario
  de datos, matriz de cobertura, nota corta).
- `references/criterios-de-calidad.md` — rúbrica final y señales de un caso mediocre.
- `references/glosario.md` — glosario ES/EN organizado por fase.
- `assets/ejemplo-aplicado.md` — el framework aplicado a un caso real, de punta a punta.
- `assets/briefs-capstone.md` — dos casos listos para ejecutar (Cyclistic y Bellabeat).
