# Elegir el caso de estudio

Fase 0: lo que ocurre **antes** de Preguntar. Elegir mal el caso cuesta una semana de trabajo que no
suma nada al portafolio, y es un error que no se detecta hasta el final.

---

## 1. El escenario base

El planteamiento que propone el Capstone y que conviene mantener como marco mental:

> Eres analista de datos junior en una consultora de inteligencia de negocio. Llevas seis meses en el
> puesto y tu jefe cree que estás listo para más responsabilidad. Te asigna liderar un proyecto para
> un cliente nuevo: desde definir la tarea de negocio hasta presentar recomendaciones basadas en
> datos. Eliges el tema, formulas las preguntas, identificas un dataset y verificas su integridad,
> haces el análisis, creas las visualizaciones y preparas la presentación.

Este encuadre importa porque **fuerza un cliente**. Sin cliente no hay decisión que habilitar, y sin
decisión la fase 6 se queda en hallazgos.

---

## 2. Calibrar el alcance

Dos referencias del certificado que funcionan bien como límites:

- **Una semana de trabajo** es un objetivo razonable para un caso completo.
- **Una presentación de ~30 minutos.** Si el tema no da para eso, es demasiado simple. Si no cabe,
  es demasiado complejo.

Señales de que el caso es **demasiado simple:**

- La respuesta se ve en una tabla dinámica de cinco minutos.
- Solo hay un hallazgo posible y es obvio antes de mirar los datos.
- No hay ninguna decisión de limpieza que documentar.
- No existe ninguna interpretación alternativa que descartar.

Señales de que es **demasiado complejo:**

- Necesitas combinar más de tres fuentes que no comparten clave.
- La pregunta requiere modelado predictivo o inferencia causal seria.
- No hay dato público disponible y tendrías que recolectarlo.
- Llevas tres días en la fase 2 y aún no confías en los datos.

Si estás entre los dos, **empieza por el más simple**. Un caso terminado, documentado y publicado
vale más que dos ambiciosos a medias.

---

## 3. Cómo elegir el tema

### Regla de oro: primero el problema de negocio, después el dataset

Si eliges los datos primero, terminas respondiendo lo que los datos permiten en lugar de lo que un
negocio necesitaría. Se nota, y es el defecto más común en los portafolios junior.

Método en tres pasos:

1. **Escribe cinco preguntas de negocio** de sectores que te interesen, sin pensar en datos.
2. **Para cada una, escribe qué decisión concreta habilitaría** la respuesta. Descarta las que no
   habiliten ninguna.
3. **Solo entonces busca datos** para las que sobrevivan. Si no hay dato disponible para ninguna,
   vuelve al paso 1 con temas más cercanos a lo que se publica abiertamente.

### Ejemplos de tareas de negocio con el alcance correcto

Del propio material del certificado, útiles como calibración:

- **Rankings deportivos universitarios.** Una empresa quiere patrocinar jugadores. Analizando varios
  años, ¿qué equipos que empiezan la temporada en el top 5 mantienen o mejoran posición? ¿Cuáles
  tienen potencial de patrocinio?
- **Expansión en alquiler vacacional.** Una gestora inmobiliaria evalúa entrar en una zona nueva. Con
  datos públicos de Airbnb: ¿cómo influyen barrio y amenidades en el precio? ¿qué anuncios se alquilan
  más? ¿dónde se concentran los superanfitriones?
- **Clima y patrones de compra.** ¿El frío aumenta la demanda de bufandas y sopa? ¿El calor la de
  ventiladores? ¿El clima severo dispara el agua embotellada y las pilas? Con datos meteorológicos
  públicos cruzados con ventas.

Nota deliberada: estos ejemplos **no vienen atados a un dataset concreto**, para que el tema no lo
elija el dato disponible.

### Criterios de selección: puntúa cada candidato

| Criterio | Pregunta | Peso |
|---|---|---|
| **Decisión** | ¿Hay una decisión de negocio concreta al final? | Eliminatorio |
| **Datos** | ¿Existe una fuente pública, creíble y con licencia clara? | Eliminatorio |
| **Suciedad útil** | ¿Los datos necesitan limpieza real que puedas documentar? | Alto |
| **Diferenciación** | ¿Demuestra algo que tus otros casos no muestran? | Alto |
| **Interés propio** | ¿Podrás hablar de esto 30 minutos sin aburrirte? | Alto |
| **Saturación** | ¿Cuántos miles de portafolios usan este mismo dataset? | Medio (a la baja) |
| **Dominio** | ¿Entiendes el sector lo suficiente para interpretar? | Medio |

Sobre **saturación**: los datasets del propio Capstone (Cyclistic, Bellabeat) están en miles de
portafolios. No los descartes — son excelentes como primer caso porque el brief es realista y el
alcance está probado —, pero tu segundo o tercer caso gana mucho con datos menos transitados.

---

## 4. Catálogo de fuentes de datos

Datasets que el propio certificado propone, todos con licencia clara:

| Fuente | Contenido | Licencia |
|---|---|---|
| **World Happiness Report** (Sustainable Development Solutions Network) | Datos regionales de felicidad, dinero, salud y otras métricas | CC0 |
| **Avocado Prices** (Justin Kiggins) | Precios y ventas históricas de aguacate en supermercados de EE. UU. | CC0 |
| **Movies Dataset** (Rounak Banik) | Metadatos de 45.000 películas: reparto, equipo, presupuesto, ingresos, valoraciones | CC0 |
| **Amazon Top 50 Best Selling Books** (Souter Saalu) | Superventas de Amazon 2009–2019, ficción y no ficción | CC0 |

Repositorios generales donde buscar:

- **Kaggle Datasets** — enorme, con licencia visible por dataset. Verifica siempre la procedencia
  original; muchos son copias de copias y fallan la **O** de ROCCC.
- **Google Dataset Search** — buscador federado.
- **Data.gov**, **datos.gob.es**, **datos.gov.co** y equivalentes nacionales — datos oficiales,
  normalmente los más creíbles.
- **Banco Mundial**, **OCDE**, **Eurostat**, **ONU** — series largas y comparables entre países.
- **NOAA** (meteorología), **INSIDE AIRBNB** (alquiler vacacional), **GBIF** (biodiversidad).
- **BigQuery public datasets** — si quieres demostrar SQL sobre volumen real.
- **Portales de datos abiertos de tu ciudad** — infrautilizados, y el conocimiento local del dominio
  juega a tu favor en la interpretación.

**Antes de comprometerte con un dataset**, ejecuta la prueba de integridad inicial de la fase 2
(volumen, rango temporal, nulos, unicidad de clave, extremos). Descubrir en la fase 4 que falta la
columna clave es el fallo más caro del proceso.

---

## 5. Ficha de decisión del caso

Rellénala antes de abrir un solo archivo. Si no puedes completarla, el caso no está listo.

```markdown
## Ficha de decisión — [nombre del caso]

**Fecha:**

### El caso
- **Sector / cliente ficticio:**
- **Problema de negocio en una frase:**
- **Decisión concreta que habilita:**
- **Audiencia de la presentación:**

### Los datos
- **Fuente candidata:**
- **Licencia:**
- **Periodo y volumen:**
- **Prueba de integridad inicial:** ✅ / ⚠️ — [qué salió]
- **¿Contiene los campos que la pregunta exige?** sí / no — [cuáles faltan]

### Calibración
- **Estimación de esfuerzo:** [días]
- **¿Da para 30 minutos de presentación?** sí / no
- **¿Hay limpieza real que documentar?** sí / no

### Encaje en el portafolio
- **Qué demuestra que mis otros casos no:**
- **Herramienta principal:** [hoja / SQL / Python / Tableau]
- **Nivel de saturación del dataset:** bajo / medio / alto

### Decisión
- [ ] Adelante
- [ ] Descartado — motivo:
```

---

## 6. Entregables del caso completo

Los siete que define el Capstone. Sirven como definición de "terminado":

1. Un enunciado claro de la tarea de negocio elegida.
2. Una descripción de todas las fuentes de datos usadas.
3. Documentación de toda limpieza o manipulación de datos.
4. Un resumen del análisis.
5. Visualizaciones de apoyo y hallazgos clave.
6. Una lista de entregables adicionales que serían útiles para explorar más.
7. Tus conclusiones de alto nivel basadas en el análisis.

---

## Puerta de salida de la fase 0

- [ ] Ficha de decisión completa.
- [ ] Problema de negocio escrito **antes** de mirar ningún dataset.
- [ ] Decisión concreta que la respuesta habilitará, identificada.
- [ ] Fuente con licencia verificada y prueba de integridad inicial pasada.
- [ ] Alcance calibrado: da para ~30 minutos y ~1 semana.
- [ ] Escrito qué demuestra este caso frente a los que ya tienes.

## Errores comunes

- Empezar por "encontré un dataset interesante".
- Elegir un tema del que no sabes nada: no podrás distinguir un hallazgo de un artefacto.
- Elegir un problema tan grande que la fase 2 nunca termina.
- No verificar la licencia hasta el momento de publicar.
- Repetir el mismo tipo de caso, la misma herramienta y el mismo tipo de dato que ya tienes.
- Descartar un tema por no tener datos perfectos: los datos imperfectos, bien declarados, son
  material de portafolio de primera.
