# caso-de-estudio-datos

Framework reutilizable para ejecutar casos de estudio de análisis de datos con las seis fases del
proceso de análisis: **Preguntar, Preparar, Procesar, Analizar, Compartir y Actuar**.

Cada fase tiene entregable definido, checklist de puerta de salida, errores comunes y plantillas
copiables. Está pensado para producir casos de portafolio defendibles, no solo análisis internos.

## Contenido

```
caso-de-estudio-datos/
├── SKILL.md                          # orquestador: reglas, flujo y cuándo usar cada referencia
├── references/
│   ├── eleccion-del-caso.md          # FASE 0 — elegir tema, calibrar alcance, datasets públicos
│   ├── 01-preguntar.md               # tarea de negocio, SMART, partes interesadas, métricas
│   ├── 02-preparar.md                # fuentes, ROCCC, sesgo, licencia, organización
│   ├── 03-procesar.md                # integridad, datos sucios, herramientas, bitácora
│   ├── 04-analizar.md                # organizar, calcular, verificar, documentar
│   ├── 05-compartir.md               # audiencia, McCandless, diseño, accesibilidad, Q&A
│   ├── 06-actuar.md                  # hallazgo → insight → recomendación, publicación
│   ├── portafolio.md                 # FASE 7 — el conjunto, la presentación, la búsqueda de empleo
│   │
│   ├── anexo-sql.md                  # estilo, JOINs, agregación, CTEs, exploración
│   ├── anexo-hojas-de-calculo.md     # errores y arreglos, funciones, tablas dinámicas
│   ├── anexo-python.md               # pandas de punta a punta, estructura del notebook
│   ├── anexo-visualizacion.md        # selector de gráfico, diseño, accesibilidad, Tableau
│   │
│   ├── plantillas.md                 # 13 plantillas copiables
│   ├── criterios-de-calidad.md       # rúbrica y revisión final
│   └── glosario.md                   # glosario ES/EN por fase
└── assets/
    ├── ejemplo-aplicado.md           # el framework recorrido de punta a punta
    └── briefs-capstone.md            # Cyclistic y Bellabeat, listos para ejecutar
```

**Divulgación progresiva:** no cargues todo a la vez. `SKILL.md` siempre, el archivo de la fase
actual, y el anexo de la herramienta cuando toque. Es lo que mantiene la calidad de las respuestas.

## Cómo usarlo

### Claude Code

Coloca la carpeta en `.claude/skills/` del proyecto (o en `~/.claude/skills/` para tenerla
disponible siempre). Se activa sola cuando menciones un caso de estudio, un dataset o un análisis.
También puedes forzarla:

```
Usa la skill caso-de-estudio-datos. Vamos a empezar la fase 1 sobre [tema].
```

### Proyectos de Claude

Sube todos los archivos al conocimiento del proyecto y pon en las instrucciones del proyecto:

```
Sigue el framework de SKILL.md para todo trabajo de análisis. Lee el archivo de referencia
de la fase antes de ejecutarla. No avances de fase sin pasar su puerta de salida.
```

### Otras herramientas LLM

Son archivos Markdown planos, sin dependencias. Pega `SKILL.md` como instrucción de sistema y
adjunta la referencia de la fase en la que estés trabajando. La divulgación progresiva —cargar solo
la fase actual— mantiene el contexto manejable y mejora la calidad de las respuestas.

### Sin LLM

Funciona como manual de trabajo. Las checklists de puerta de salida y las plantillas son útiles
por sí solas.

## Dónde vive esta carpeta

`caso-de-estudio-datos/` se instala **una sola vez, al nivel del portafolio** — no dentro de cada
caso:

```
portafolio/
├── framework/
│   └── caso-de-estudio-datos/    <- esta carpeta, una sola copia
├── site/                         <- el sitio publicado
└── cases/
    ├── caso-1/
    ├── caso-2/
    └── caso-3/
```

Si aparece una segunda copia dentro de la carpeta de un caso, es un error, no una variante: bórrala
y deja solo esta. Dos copias divergen en semanas y dejan de estar claro cuál manda.

El detalle completo de la estructura de cada caso (`CASO.md`, `documentacion/`, `datos/`, etc.) está
en la sección "Estructura de archivos recomendada" de `SKILL.md`, junto con el traspaso al sitio.

## Arranque rápido

**Si ya tienes tema y datos:**

1. Crea la carpeta del caso dentro de `cases/`, con la estructura que indica `SKILL.md`.
2. Copia la plantilla de `CASO.md` desde `references/plantillas.md`.
3. Abre `references/01-preguntar.md` y trabaja la fase 1 hasta pasar su puerta de salida.
4. Repite por fase, leyendo el anexo de la herramienta cuando llegues a Procesar y Analizar.
   Actualiza `CASO.md` al cerrar cada una.
5. Antes de publicar, pasa por `references/criterios-de-calidad.md`.
6. Cierra con `references/portafolio.md`: qué demuestra este caso y cómo se presenta.

**Si no tienes tema todavía:** empieza por `references/eleccion-del-caso.md` y rellena la ficha de
decisión antes de abrir un solo archivo de datos.

**Si quieres practicar sin decidir nada:** usa uno de los dos briefs de `assets/briefs-capstone.md`.

## Origen

Basado en el proceso de análisis de datos del certificado Google Data Analytics, en los materiales
de sus ocho partes y en la estructura de casos de estudio de su Capstone, reorganizado como framework
operativo con puertas de calidad.
