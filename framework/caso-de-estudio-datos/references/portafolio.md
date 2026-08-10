# Portafolio y presentación

Lo que ocurre **después** de la fase 6, cuando el caso ya está publicado: cómo encaja en el conjunto,
cómo se presenta y cómo se usa en una búsqueda de empleo.

`06-actuar.md` cubre publicar *un* caso. Este archivo cubre la estrategia del **conjunto**.

---

## 1. El portafolio como argumento, no como archivo

Un portafolio no es una carpeta de proyectos: es un argumento sobre qué sabes hacer. Tres o cuatro
casos que demuestran cosas distintas superan a ocho que demuestran lo mismo.

**Matriz de cobertura.** Rellénala con lo que ya tienes y usa los huecos para elegir el siguiente
caso:

| Caso | Tipo de problema | Herramienta principal | Dominio | Tipo de dato | Qué demuestra |
|---|---|---|---|---|---|
| Caso 1 | | | | | |
| Caso 2 | | | | | |
| Caso 3 | | | | | |

Ejes que conviene cubrir entre todos:

- **Tipo de problema:** predecir, categorizar, detectar lo inusual, identificar temas, descubrir
  conexiones, encontrar patrones.
- **Herramienta:** hoja de cálculo, SQL, Python, Tableau. Al menos un caso donde SQL o Python sean
  protagonistas.
- **Tipo de dato:** transversal vs longitudinal; estructurado vs semiestructurado; una fuente vs
  varias combinadas.
- **Naturaleza del hallazgo:** al menos un caso donde el resultado **contradiga** la hipótesis
  inicial. Es el más valioso de todos, porque demuestra que no fuerzas la conclusión.

Antes de empezar un caso nuevo, escribe en una frase qué casilla llena. Si no llena ninguna, el
esfuerzo rinde más en otro ángulo.

---

## 2. Dónde vive el portafolio

| Opción | Fuerte en | Débil en |
|---|---|---|
| **GitHub** | Reproducibilidad, código visible, estándar del sector | Poco narrativo por sí solo; los recruiters no técnicos no lo leen |
| **Sitio propio** (GitHub Pages, Notion, Carrd) | Narrativa, diseño, primera impresión | Requiere mantenimiento; no muestra el código |
| **Kaggle Notebooks** | Comunidad, ejecución en línea | Todo se ve igual; poco diferenciador |
| **Tableau Public** | Interactividad, muy visual | Solo la parte de visualización |

Combinación que funciona: **un sitio propio narrativo** que presenta los casos con su titular y su
gráfico principal, y **un repositorio por caso** para el detalle reproducible.

### Las tres capas de un caso publicado

El framework ya aplica divulgación progresiva a cómo se *lee* la documentación. La misma idea
gobierna cómo se *publica*: tres capas, tres audiencias, tres tiempos de lectura.

| Capa | Quién lee | Tiempo | Qué es | Dónde vive |
|---|---|---|---|---|
| **L1 — Tarjeta** | Reclutador escaneando | 15 s | Titular + resumen + gráfico principal | Home del sitio |
| **L2 — Caso** | Hiring manager | 5 min | La narrativa completa | Página del caso, en el sitio |
| **L3 — Evidencia** | Analista que valida | 30 min | `CASO.md`, bitácora, notebooks, datos | Repositorio del caso |

**El sitio publica L1 y L2. L3 se queda en el repositorio.** Nadie lee un `CASO.md` de 400 líneas
en una web; quien quiere ese nivel de detalle sabe ir a buscarlo, y encontrarlo allí completo es
justo lo que separa un caso defendible de una galería de gráficos.

**L1 no se escribe aparte: se genera del front-matter de L2.** Redactar la tarjeta del índice por
separado es la vía más rápida a que el titular del índice y el del caso dejen de coincidir.

### El contrato de contenido

Para que publicar el caso siguiente no obligue a rediseñar nada, cada caso entrega **un** Markdown
con este front-matter. El sitio lo valida contra un esquema: si falta un campo obligatorio, la
construcción falla. Es la puerta de salida de la fase 7, aplicada por código en vez de por
buena voluntad.

```yaml
---
title:        # EL HALLAZGO, no el tema. Es el titular de L1 y de L2.
summary:      # 2-3 frases -> el párrafo de la tarjeta L1
hero:         # ruta a la visualización principal
heroAlt:      # texto alternativo real, no el nombre del archivo
date:         # AAAA-MM-DD
tools:        # [Python, pandas, matplotlib]
domain:       # sector del caso
problemType:  # taxonomía de la fase 1: encontrar patrones, predecir, categorizar...
scale:        # "125.855 juegos · 2 fuentes" — da la medida de un vistazo
repo:         # URL del repositorio de evidencia (L3)
featured:     # true -> aparece en la home
demonstrates: # qué demuestra este caso que los demás no
---
```

`problemType`, `domain`, `tools` y `demonstrates` son los mismos ejes de la matriz de cobertura
de la sección 1. No es casualidad: **la matriz se puede generar a partir de los front-matter**,
en vez de mantenerse a mano y quedar desactualizada al tercer caso.

### El traspaso: qué cruza del repositorio al sitio

Regla dura: **el sitio solo transporta agregados, nunca datos crudos ni intermedios.**

| Del repositorio del caso | Al sitio | Tamaño típico |
|---|---|---|
| El Markdown de L2 con su front-matter | La página del caso | KB |
| `salidas/graficos/*.png` | Imágenes de la página | cientos de KB |
| `salidas/tablas/*.csv` → JSON | Fuente de un gráfico interactivo | KB |
| `datos/`, notebooks, `CASO.md` | **No cruzan.** Se enlazan | — |

Si un agregado que necesita el sitio pesa megas, la agregación está incompleta: vuelve a la fase 4
y resúmelo más, en vez de subir el peso al sitio.

### Antes de publicar: revisa rutas y secretos

El error más caro es el más aburrido. Antes de hacer público un repositorio, busca literalmente
rutas absolutas en todo el árbol:

```bash
grep -rn "/home/\|/Users/\|C:\\\\\|/sessions/\|/mnt/" --include="*.py" --include="*.js" \
     --include="*.ipynb" --include="*.md" .
```

Un script con la ruta de la máquina donde se escribió no es reproducible por nadie, y es lo
primero que rompe cuando alguien clona el repositorio para comprobar tu trabajo. Todas las rutas
se resuelven desde la ubicación del propio script; todas las imágenes de los Markdown son
relativas.

### Ejemplo de resumen para la tarjeta L1

> **Los usuarios casuales de Cyclistic viajan 2,3× más tiempo y se concentran en fines de semana.**
> Analicé 5,7 millones de viajes de 12 meses con Python y pandas para entender en qué se diferencia
> el uso de miembros anuales y usuarios casuales. Descubrí que los casuales usan el servicio por
> ocio, no para desplazarse, lo que invalidaba el supuesto sobre el que se había planteado la
> campaña. Recomendé una membresía de fin de semana con lanzamiento en jueves y promoción en
> estaciones de ocio. `Python` `pandas` `matplotlib`

---

## 3. La presentación

### Conoce tu flujo

Una buena historia de datos necesita **trama** (tema y flujo), **diálogo** (puntos de conversación) y
**final** (resultados y conclusiones). Dos preguntas definen el flujo:

**¿Quién es la audiencia?**

- **Ejecutivos, consejo, dirección (C-level):** nivel alto. Quieren la historia, no *toda* la
  historia. Se enfocan en mejorar, corregir o inventar cosas. Brevedad, y la mayor parte del tiempo
  en resultados y recomendaciones.
- **Partes interesadas y managers:** tienen más tiempo y harán preguntas específicas sobre los datos.
  Prepara puntos de conversación sobre los aspectos del análisis que llevaron a las conclusiones.
- **Otros analistas y colaboradores individuales:** la mayor libertad y el mayor tiempo. Puedes
  profundizar en datos, procesos y resultados.

**¿Cuál es el propósito?**

- **Pedir o recomendar algo:** cada lámina trabaja hacia la propuesta final.
- **Enfocarse en resultados:** cada lámina marca el camino hacia el resultado. Deja "migas de pan"
  —vistas de los pasos del análisis— que muestren el recorrido.
- **Reportar el análisis:** las láminas resumen datos y hallazgos con claridad. Aquí está bien que
  los datos hablen por sí mismos.

### Prepara puntos de conversación y limita el texto

Tu audiencia lee la lámina **mientras** hablas. Si la lámina se parece a un documento, reescribe lo
que vas a decir y quita texto.

**Regla de los cinco segundos:** nadie debería tardar más de cinco segundos en leer un bloque de
texto de una lámina.

Lo que lees en la lámina y lo que dices **no deben ser lo mismo**. Debe haber equilibrio entre las
dos. Nunca leas la lámina en voz alta.

Saber exactamente qué vas a decir en cada lámina crea un flujo natural y evita las pausas incómodas.
Puntos de conversación variados mantienen despierta a la audiencia en las láminas de resumen, que
tienden a ser repetitivas.

### Termina con la propuesta

- **Una lámina para la propuesta**, al final. Clara y concisa. Ya llevaste a la audiencia por el
  recorrido; ahora haz explícita la recomendación.
- Si recomiendas hacer algo, **incluye próximos pasos y qué considerarías un resultado exitoso**.

### Estructura del mazo

| # | Lámina | Contenido |
|---|---|---|
| 1 | **Agenda** | Temas y tiempo por tema |
| 2 | **Propósito** | Por qué existe el proyecto y por qué le importa al negocio |
| 3–n | **La historia de datos** | Se puede en una sola lámina si resumes bien; si son varias, cada una introduce lógicamente a la siguiente |
| n+1 | **La propuesta** | La recomendación, explícita |
| n+2 | **Llamada a la acción** | Qué debe pasar ahora. Puede fusionarse con la anterior si es una sola acción |
| — | **Anexos** | Todo el detalle que anticipas que preguntarán |

Agenda de ejemplo para 30 minutos:

- Presentaciones — 4 min
- Visión general y objetivos del proyecto — 5 min
- Datos y análisis — 10 min
- Recomendación — 3 min
- Pasos accionables — 3 min
- Preguntas — 5 min

### Tiempo

Asume que todos en la sala están ocupados.

- Vigila el tiempo total y el de cada lámina.
- Cada lámina debe contar una parte **única** de la historia. Si una no es única, fúsionala con otra.
- **Reserva tiempo para preguntas**, al final o durante.

### Animaciones con propósito

- Aparecer los puntos de uno en uno mientras los explicas.
- Mostrar solo el elemento visual relevante y atenuar el resto.
- Flechas o llamadas señalando la zona concreta del gráfico de la que hablas.

Nada más. La animación por defecto de la herramienta distrae.

---

## 4. Las tres versiones que necesitas ensayar

| Versión | Duración | Cuándo | Contenido |
|---|---|---|---|
| **Completa** | ~30 min | Presentación formal, entrevista técnica final | El mazo completo con anexos |
| **Corta** | 3 min | Entrevistas, networking. **La que más vas a usar** | Contexto, pregunta, hallazgo principal, recomendación, limitación |
| **Una frase** | 15 s | "Cuéntame un proyecto tuyo" | El titular con la conclusión |

**Ensáyalas por separado.** La versión de tres minutos no es la de treinta acelerada: es una pieza
distinta que hay que construir aparte. Ensáyala en voz alta, con alguien que no sea del sector.

**Prepara el Q&A por escrito.** Las cinco preguntas más incómodas — calidad de los datos, causalidad,
por qué descartaste una alternativa, qué costaría implementarlo, qué harías distinto — con su
respuesta lista. Es la diferencia entre un análisis que se aprueba y uno que se devuelve.

Ten **varias formas de decir lo mismo**. Si alguien no entiende una explicación, una segunda
formulación suele resolverlo.

---

## 5. Después de presentar: pide retroalimentación

Pregunta a tu manager o a otro analista qué opinan con franqueza de cómo contaste la historia y de la
presentación en conjunto. La retroalimentación es lo que hace que la siguiente sea mejor.

---

## 6. Usar el portafolio en la búsqueda de empleo

- **En el CV:** enlace al índice del portafolio, no a un repositorio suelto. En la descripción de tus
  proyectos, escribe el resultado, no la tarea: "identifiqué que el 68 % de los casuales viaja en
  fin de semana, base de una recomendación de membresía segmentada", no "analicé datos de viajes".
- **En LinkedIn:** un post por caso, con el titular, el gráfico principal y el enlace. Es la vía por
  la que más gente lo verá.
- **En la entrevista:** lleva la versión de tres minutos preparada. Espera preguntas sobre
  limitaciones — y que las tengas escritas juega a tu favor.
- **Comunidad:** participar en comunidades de datos, comentar el trabajo de otros y recibir crítica
  sobre el tuyo mejora el portafolio más rápido que hacer un caso más en solitario.

---

## Puerta de salida del portafolio

- [ ] Matriz de cobertura rellena; cada caso demuestra algo distinto.
- [ ] Cada caso cumple el contrato: front-matter completo y las siete secciones en orden.
- [ ] La tarjeta L1 se genera del front-matter — no hay una versión escrita a mano en paralelo.
- [ ] La construcción del sitio pasa. Un caso al que le falte un campo obligatorio debe **romperla**;
      si no la rompe, el esquema no está haciendo su trabajo.
- [ ] Todos los enlaces funcionan y las imágenes se ven sin descargar nada.
- [ ] Ningún repositorio contiene datos sensibles, credenciales ni rutas locales.
      Comprobado con el `grep` de rutas absolutas de la sección 2, no de memoria.
- [ ] El sitio no transporta datos crudos ni intermedios: solo agregados de kilobytes.
- [ ] Leído en un teléfono real. Los reclutadores abren los enlaces desde el móvil.
- [ ] Las tres versiones de la presentación ensayadas en voz alta.
- [ ] Q&A escrito para las cinco preguntas más difíciles de cada caso.
- [ ] Al menos un caso donde el resultado contradijo la hipótesis inicial.
- [ ] Retroalimentación pedida a alguien externo, y aplicada.

## Errores comunes

- Publicar el notebook sin narrativa y llamarlo caso de estudio.
- Un índice que lista nombres de proyecto en vez de conclusiones.
- **Escribir la tarjeta L1 aparte del caso.** A los dos meses dicen cosas distintas.
- **Subir al sitio los datos del análisis** en vez de los agregados. El sitio se vuelve lento y el
  repositorio deja de ser la única fuente de verdad de los datos.
- **Dejar rutas absolutas en el código publicado.** Convierte un análisis reproducible en uno que
  solo corría en la máquina donde se escribió — y no se nota hasta que alguien intenta clonarlo.
- **Rehacer la estructura en cada caso.** Si el caso 2 no encaja en el contrato, lo que hay que
  discutir es el contrato, no improvisar una excepción.
- Cuatro casos que usan la misma herramienta sobre el mismo tipo de dato.
- Ensayar solo la versión larga y improvisar la corta, que es la que de verdad se usa.
- Leer las láminas en voz alta.
- Láminas que son documentos: la audiencia lee en vez de escuchar.
- No dejar tiempo para preguntas.
- Esconder las limitaciones. Es el primer sitio donde un entrevistador con criterio va a mirar.
