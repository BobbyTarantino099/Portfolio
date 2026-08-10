# Plantillas

Plantillas copiables para los entregables de cada fase. Copia el bloque, no lo reescribas.

## Índice

1. [CASO.md — artefacto vivo](#1-casomd--artefacto-vivo)
2. [Ficha de fuente de datos](#2-ficha-de-fuente-de-datos)
3. [Diccionario de datos](#3-diccionario-de-datos)
4. [Bitácora de limpieza](#4-bitácora-de-limpieza)
5. [Registro de hallazgo](#5-registro-de-hallazgo)
6. [Ficha de recomendación](#6-ficha-de-recomendación)
7. [Página de caso para el sitio (L2)](#7-página-de-caso-para-el-sitio-l2)
8. [Guion de presentación](#8-guion-de-presentación)
9. [Hoja de ruta del caso — preguntas guía por fase](#9-hoja-de-ruta-del-caso--preguntas-guía-por-fase)
10. [Alcance del trabajo (SOW)](#10-alcance-del-trabajo-sow)
11. [Diario de datos](#11-diario-de-datos)
12. [Matriz de cobertura del portafolio](#12-matriz-de-cobertura-del-portafolio)
13. [Nota corta](#13-nota-corta)

---

## 1. CASO.md — artefacto vivo

```markdown
# Caso: [nombre]

**Estado:** fase [N] — [nombre de la fase]
**Última actualización:** AAAA-MM-DD

## 1. Preguntar
- **Problema de negocio:**
- **Pregunta analítica (SMART):**
- **Decisión que habilita:**
- **Tipo de problema:**
- **Partes interesadas:** [quién · qué decide · qué necesita ver]
- **Métricas:** [nombre · fórmula · unidad · granularidad · ventana]
- **Fuera de alcance:**
- **Puerta de salida:** ✅ / ⬜ + qué falta

## 2. Preparar
- **Fuentes:** [ver fichas abajo]
- **Evaluación ROCCC:**
- **Sesgos identificados:**
- **Licencia / privacidad:**
- **Prueba de integridad inicial:**
- **Puerta de salida:** ✅ / ⬜

## 3. Procesar
- **Herramienta y justificación:**
- **Bitácora:** [enlace a bitacora-limpieza.md]
- **Reconciliación de conteos:** N inicial − N eliminadas = N final
- **Puerta de salida:** ✅ / ⬜

## 4. Analizar
- **Estadística descriptiva:**
- **Hallazgos:** [ver registros]
- **Verificaciones aplicadas:**
- **Lo que los datos no responden:**
- **Puerta de salida:** ✅ / ⬜

## 5. Compartir
- **Audiencia(s):**
- **Visualizaciones:** [lista con su titular]
- **Q&A preparado:**
- **Puerta de salida:** ✅ / ⬜

## 6. Actuar
- **Recomendaciones:** [ver fichas]
- **Limitaciones:**
- **Datos adicionales deseables:**
- **Publicado en:** [enlace]
- **Puerta de salida:** ✅ / ⬜

## Bitácora de decisiones
| Fecha | Decisión | Motivo | Alternativa descartada |
|---|---|---|---|
```

---

## 2. Ficha de fuente de datos

```markdown
### Fuente: [nombre]
- **Origen:** primera / segunda / tercera parte — [entidad]
- **URL o ubicación:**
- **Fecha de descarga:**
- **Licencia:** [nombre + qué permite]
- **Periodo cubierto:**
- **Granularidad:** [una fila = ...]
- **Volumen:** N filas × M columnas
- **Formato:**
- **ROCCC:** R:__ O:__ C:__ C:__ C:__ — fallas: [cuáles y su efecto]
- **PII presente:** sí / no — tratamiento:
- **Limitaciones conocidas:**
```

---

## 3. Diccionario de datos

```markdown
| Columna | Tipo | Unidad | Valores permitidos | Significado | Nulos |
|---|---|---|---|---|---|
```

---

## 4. Bitácora de limpieza

```markdown
# Bitácora de limpieza — [caso]

**Dataset de entrada:** [archivo] — N filas
**Dataset de salida:** [archivo] — M filas
**Herramienta:**

## Transformaciones

### T1 — [título corto]
- **Qué:**
- **Por qué:**
- **Cómo:** [fórmula / consulta / código]
- **Filas afectadas:** N (X % del total)
- **Alternativa descartada:** [y por qué]

### T2 — ...

## Reconciliación
| Concepto | Filas |
|---|---|
| Iniciales | |
| Eliminadas por duplicados | |
| Eliminadas por valores imposibles | |
| Eliminadas por nulos críticos | |
| **Finales** | |

## Verificación posterior
- [ ] Conteos cuadran
- [ ] Categorías estandarizadas son las esperadas
- [ ] Rangos numéricos plausibles
- [ ] Proceso reproducible desde el crudo
- [ ] Dataset limpio sigue respondiendo la pregunta
```

---

## 5. Registro de hallazgo

```markdown
### H[N] — [titular que enuncia el hallazgo]
- **Pregunta que responde:**
- **Cálculo:** [fórmula / consulta / celda]
- **Resultado:** [cifra + unidad]
- **Subconjunto usado:**
- **Interpretación (una frase):**
- **Verificaciones:** sensatez ⬜ · recálculo alterno ⬜ · desagregación ⬜
- **Lecturas alternativas descartadas:**
```

---

## 6. Ficha de recomendación

```markdown
### R[N] — [acción en imperativo]
- **Acción:** qué, quién, cuándo
- **Evidencia:** [H[N] — cifra concreta]
- **Impacto esperado:** [magnitud] — supuesto: [de dónde sale]
- **Métrica de éxito:** [métrica] evaluada a [plazo]
- **Riesgo / supuesto crítico:**
- **Esfuerzo:** alto / medio / bajo
```

---

## 7. Página de caso para el sitio (L2)

Este es **el** entregable publicable del caso: un solo Markdown que alimenta a la vez la página
del caso y su tarjeta en la home. El contrato completo y el porqué de las tres capas están en
`portafolio.md`, sección 2.

El texto va **en inglés** porque es lo que se publica. Lo que está entre corchetes son
instrucciones, no contenido.

El orden de las secciones es fijo. No es rigidez decorativa: es lo que hace que abrir el caso 5
se sienta igual que abrir el caso 1, y lo que permite meter un caso nuevo sin tocar el sitio.

````markdown
---
title: "[The finding, not the topic. One sentence a recruiter can repeat out loud.]"
summary: "[2-3 sentences: what you analysed, what you found, what you recommended.]"
hero: "./images/01-key-chart.png"
heroAlt: "[What the chart shows, written for someone who cannot see it.]"
date: YYYY-MM-DD
tools: [Python, pandas, matplotlib]
domain: "[Sector]"
problemType: "[find patterns | predict | categorize | spot something unusual | identify themes | discover connections]"
scale: "[125,855 games · 2 sources]"
repo: "https://github.com/[user]/[case-repo]"
featured: true
demonstrates: "[The specific skill this case shows that the others do not.]"
---

## Context

[The business problem and the analytical question. Two paragraphs maximum: who had to decide
what, and why data could answer it.]

## Data

| Source | Period | Volume | Licence |
|---|---|---|---|

[If a source is too large to publish, say so here and link to where it can be downloaded.]

**Main limitations:** [The three or four that actually matter. Declaring them builds credibility;
hiding them destroys it the moment someone asks.]

## Process

**Tools:** [What, and why. The "why" is where judgement shows.]

**Key cleaning decisions:**

1. [The decision, and what it would have broken had you not made it.]

[Count reconciliation: initial − excluded = final. Full detail in the cleaning log.]

## Findings

### 1. [Headline that states the finding]

![Alt text describing the chart](./images/01-key-chart.png)

[One or two sentences of interpretation. The chart shows; the text says what it means.]

### 2. [Second finding]

[Report the finding that did NOT fit the conclusion too. Omitting it is the easiest mistake to
make and the most expensive when someone notices.]

## Recommendations

| # | Recommendation | Evidence | Impact | Effort |
|---|---|---|---|---|

[Each row is an action, not an observation. "Users travel more at weekends" is a finding;
"launch the campaign on Thursday" is a recommendation. Full cards live in the case repo.]

**Next step:** [The one thing you would do next, and what decision it unlocks.]

## Reproduce

```bash
git clone [repo-url]
# dependencies, data download, scripts in order
```

## What this demonstrates

[Be concrete. Not "data cleaning" but what was genuinely hard here and how you handled it.]
````

---

## 8. Guion de presentación

```markdown
# Guion — [caso]

**Duración objetivo:** [30 min / 3 min]
**Audiencia:**

| # | Diapositiva | Mensaje único | Tiempo |
|---|---|---|---|
| 1 | Titular con la conclusión | | 1' |
| 2 | Contexto y pregunta | | 2' |
| 3 | Datos y limitaciones | | 3' |
| 4-8 | Hallazgos (uno por lámina) | | 12' |
| 9 | Recomendaciones | | 7' |
| 10 | Próximos pasos | | 2' |
| — | Anexos | | — |

## Q&A preparado
| Pregunta difícil | Respuesta | Respaldo |
|---|---|---|
| ¿Qué tan confiables son estos datos? | | |
| ¿Eso es causalidad o correlación? | | |
| ¿Qué pasa si el supuesto X no se cumple? | | |
| ¿Por qué descartaste [alternativa]? | | |
| ¿Cuánto costaría implementarlo? | | |
```

---

## 9. Hoja de ruta del caso — preguntas guía por fase

Formato del Capstone. Úsala como control rápido durante el trabajo: si no puedes responder una
pregunta guía, la fase no está cerrada. Las puertas de salida detalladas están en los archivos de
cada fase.

```markdown
### Preguntar
**Preguntas guía**
- ¿Qué tema estoy explorando?
- ¿Qué problema estoy tratando de resolver?
- ¿Qué métricas usaré para medir los datos y alcanzar el objetivo?
- ¿Quiénes son las partes interesadas?
- ¿Quién es mi audiencia?
- ¿Cómo ayudarán mis hallazgos al cliente a tomar decisiones?

**Tareas clave**
1. Identificar la tarea de negocio
2. Determinar las partes interesadas clave
3. Elegir un conjunto de datos
4. Establecer las métricas

**Entregable:** un enunciado claro de la tarea de negocio elegida

---

### Preparar
**Preguntas guía**
- ¿Dónde están los datos?
- ¿Cómo están organizados?
- ¿Hay problemas de sesgo o credibilidad? ¿Los datos cumplen ROCCC?
- ¿Cómo estoy tratando licencia, privacidad, seguridad y accesibilidad?
- ¿Cómo verifiqué la integridad de los datos?
- ¿Cómo me ayudan a responder mi pregunta?
- ¿Hay algún problema con los datos?

**Tareas clave**
- Descargar los datos y almacenarlos apropiadamente
- Identificar cómo están organizados
- Ordenar y filtrar
- Determinar la credibilidad de los datos

**Entregable:** una descripción de todas las fuentes usadas

---

### Procesar
**Preguntas guía**
- ¿Qué herramientas elijo y por qué?
- ¿He asegurado la integridad de los datos?
- ¿Qué pasos he dado para asegurar que los datos están limpios?
- ¿Cómo puedo verificar que están limpios y listos para analizar?
- ¿He documentado el proceso de limpieza para poder revisarlo y compartirlo?

**Tareas clave**
- Revisar los datos en busca de errores
- Elegir las herramientas
- Transformar los datos para poder trabajar con ellos
- Documentar el proceso de limpieza

**Entregable:** documentación de toda limpieza o manipulación de datos

---

### Analizar
**Preguntas guía**
- ¿Cómo debo organizar los datos para analizarlos?
- ¿Los datos están correctamente formateados?
- ¿Qué sorpresas descubrí?
- ¿Qué tendencias o relaciones encontré?
- ¿Cómo ayudan estos hallazgos a responder la pregunta de negocio?

**Tareas clave**
- Agregar los datos para que sean útiles y accesibles
- Organizar y formatear
- Realizar los cálculos
- Documentar los cálculos para seguir el rastro del análisis
- Identificar tendencias y relaciones

**Entregable:** un resumen del análisis

---

### Compartir
**Preguntas guía**
- ¿Pude responder la pregunta de negocio?
- ¿Qué historia cuentan mis datos?
- ¿Cómo se relacionan mis hallazgos con la pregunta original?
- ¿Quién es mi audiencia? ¿Cuál es la mejor forma de comunicarme con ella?
- ¿Puede la visualización ayudarme a compartir los hallazgos?
- ¿Mi presentación es accesible para la audiencia?

**Tareas clave**
- Determinar la mejor forma de compartir los hallazgos
- Crear visualizaciones eficaces
- Presentar los hallazgos
- Asegurar que el trabajo es accesible

**Entregable:** visualizaciones de apoyo y hallazgos clave

---

### Actuar
**Preguntas guía**
- ¿Cuál es mi conclusión final basada en el análisis?
- ¿Cómo podrían el equipo y el negocio aplicar mis hallazgos?
- ¿Qué próximos pasos daría yo, o darían las partes interesadas?
- ¿Hay datos adicionales que podría usar para ampliar los hallazgos?

**Tareas clave**
- Crear el portafolio
- Añadir el caso de estudio
- Practicar la presentación con alguien

**Entregable:** las conclusiones de alto nivel y la lista de entregables adicionales útiles
para una exploración posterior
```

---

## 10. Alcance del trabajo (SOW)

Acuerdo explícito de qué se va a hacer y — sobre todo — qué **no**. Se rellena en la fase 1. La
mayoría de los desastres de expectativas se originan por no escribir la sección "esto no incluye".

```markdown
# Proyecto de análisis de datos — [nombre]

**Analista:** [tú]
**Cliente / patrocinador:**
**Fecha:**

## Propósito
[Por qué existe este proyecto. Cuáles son los objetivos. Breve.]

## Alcance / actividades principales
[Las partes principales del proyecto: pasos, actividades o etapas de alto nivel,
con una descripción breve de cada una.]

| Actividad | Descripción |
|---|---|
| | |
| | |

## Este proyecto NO incluye
[Lo que el proyecto explícitamente no hace. Sé concreto:
"no incluye el análisis de los datos de 2019", "no incluye segmentación demográfica
porque la fuente no la contiene".]

- 
- 

## Entregables
[Lista específica de lo que el proyecto va a entregar.]

| Entregable | Descripción / detalle |
|---|---|
| | |
| | |

## Calendario e hitos principales
[Definido por hitos ("todos los datos limpios y procesados"), por periodos
("semana 1 / semana 2") u otra forma según el proyecto.]

| Hito | Fecha prevista | Descripción / detalle |
|---|---|---|
| | | |
| | | |

**Fecha estimada de finalización:**
*(la fecha de "si todo va bien y tengo todo lo que necesito, termino aquí")*

## Supuestos
[Qué tiene que ser cierto para que este calendario se cumpla.]
```

---

## 11. Diario de datos

Registro de aprendizaje y de decisiones. Fechar la entrada e incluir la pregunta permite releerlo
después y ver cómo evolucionó tu criterio. Útil también como cantera de material para el portafolio
y para responder "cuéntame algo que aprendiste" en una entrevista.

```markdown
| Fecha | AAAA-MM-DD |
|---|---|
| **Curso / tema** | |
| **Pregunta o disparador** | |
| **Entrada** | [Qué pensé, qué decidí, qué me sorprendió, qué haría distinto] |
| **Otras ideas o preguntas** | |
```

Ejemplo de entrada:

```markdown
| Fecha | 2026-07-20 |
|---|---|
| **Curso / tema** | Fase 3 — Procesar, caso Cyclistic |
| **Pregunta o disparador** | ¿Elimino los viajes de más de 24 horas o los conservo? |
| **Entrada** | Encontré 3.412 viajes de más de 24 h (0,06 %). Mi primer impulso fue borrarlos. Investigando, la mayoría son bicicletas no devueltas correctamente, no viajes reales. Decidí excluirlos del cálculo de duración pero conservarlos en el conteo de viajes, porque sí representan un uso del servicio. Documenté las dos alternativas en la bitácora. |
| **Otras ideas o preguntas** | ¿Debería reportarlos como hallazgo aparte? Un 0,06 % de bicicletas mal devueltas puede ser un problema operativo que a nadie le han contado. |
```

---

## 12. Matriz de cobertura del portafolio

Se rellena antes de empezar un caso nuevo. Si el caso candidato no llena ningún hueco, el esfuerzo
rinde más en otro ángulo. Detalle en `portafolio.md`.

```markdown
| Caso | Tipo de problema | Herramienta principal | Dominio | Tipo de dato | Qué demuestra |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

**Huecos identificados:**
- Tipo de problema sin cubrir:
- Herramienta sin demostrar:
- ¿Tengo algún caso donde el resultado contradijo la hipótesis inicial? sí / no

**El próximo caso debería:**
```

Las columnas de esta matriz son los mismos campos del front-matter del contrato (`problemType`,
`tools`, `domain`, `demonstrates`). Si el sitio ya tiene los casos publicados, la matriz se puede
**generar** a partir de ellos en vez de mantenerse a mano — que es como acaba desactualizada.

---

## 13. Nota corta

Una nota no es un caso pequeño: es una pieza suelta que no pasa por las seis fases y no pretende
hacerlo. Un truco de SQL, una lección de un caso, un gráfico que merece comentario. Sirve para
mantener el sitio vivo entre casos, que tardan semanas.

Si una nota empieza a necesitar limpieza documentada y recomendaciones, no era una nota: era un
caso. Ábrele su carpeta y empieza por la fase 0.

```markdown
---
title: "[Concrete and specific. 'Why my median was lying to me', not 'Notes on statistics'.]"
summary: "[One sentence. This is all that shows in the notes list.]"
date: YYYY-MM-DD
tags: [SQL]
---

[Three to six paragraphs. One idea, start to finish. If it needs sections, it is probably a case.]
```
