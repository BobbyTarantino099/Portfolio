# Briefs listos para ejecutar

Los dos casos estructurados del Capstone del certificado, reescritos como briefs de arranque. Sirven
para practicar el framework sin gastar tiempo en la fase 0, o como plantilla de cómo se ve un
encargo realista.

**Advertencia de saturación:** ambos aparecen en miles de portafolios. Son excelentes como *primer*
caso, porque el planteamiento es realista y el alcance está probado. Para el segundo o el tercero,
usa `references/eleccion-del-caso.md` y busca datos menos transitados. Si haces uno de estos, lo que
te diferencia no es el dataset: es el rigor de la bitácora, la calidad de los titulares y la
concreción de las recomendaciones.

---

## Brief 1 — Cyclistic: ¿cómo navega el éxito acelerado un servicio de bicicletas compartidas?

### Escenario

Eres analista de datos junior en el equipo de marketing de **Cyclistic**, una empresa de bicicletas
compartidas en Chicago. La directora de marketing cree que el futuro de la compañía depende de
maximizar las membresías anuales. Tu equipo quiere entender **en qué se diferencia el uso que hacen
los ciclistas casuales del que hacen los miembros anuales**. Con esos hallazgos diseñarán una
estrategia para convertir casuales en miembros. El equipo ejecutivo — notoriamente detallista —
debe aprobar las recomendaciones, así que tienen que estar respaldadas por datos convincentes y
visualizaciones profesionales.

### La empresa

Cyclistic lanzó su programa en 2016. Hoy tiene **5.824 bicicletas geolocalizadas** y **692
estaciones** en Chicago. Se desbloquean en una estación y se devuelven en cualquier otra. Además de
bicicletas tradicionales, ofrece reclinadas, triciclos de mano y bicicletas de carga, lo que hace el
servicio más inclusivo: **alrededor del 8 % de los usuarios** usa estas opciones asistidas. La
mayoría usa el servicio por ocio; **cerca del 30 % lo usa para ir al trabajo** a diario.

Hasta ahora la estrategia de marketing se apoyó en notoriedad general y segmentos amplios, apoyada
en la flexibilidad de precios:

- **Pases de un viaje** y **pases de un día** → estos usuarios son **ciclistas casuales**.
- **Membresías anuales** → estos usuarios son **miembros de Cyclistic**.

El área financiera concluyó que **los miembros anuales son mucho más rentables**. La directora cree
que hay una oportunidad sólida en convertir casuales — ya conocen el programa y ya eligieron
Cyclistic — en lugar de captar clientes nuevos.

### Personajes

| Quién | Rol | Qué necesita |
|---|---|---|
| **Lily Moreno** | Directora de marketing, tu jefa | Base analítica para diseñar la campaña de conversión |
| **Equipo de analítica de marketing** | Tus colegas | Método y datos reproducibles |
| **Equipo ejecutivo** | Deciden si aprueban | Evidencia sólida, visualizaciones profesionales, cero ambigüedad |

### La tarea

Tres preguntas guían el programa de marketing:

1. **¿En qué difiere el uso de las bicicletas entre miembros anuales y ciclistas casuales?**
2. ¿Por qué comprarían los casuales una membresía anual?
3. ¿Cómo puede Cyclistic usar medios digitales para influir en que los casuales se hagan miembros?

**Moreno te asignó la primera.** Es tu pregunta analítica: no intentes responder las tres.

### Datos

Datos históricos de viajes de Cyclistic (los 12 meses más recientes), publicados por Motivate
International Inc. bajo licencia pública. Nota de privacidad relevante para la fase 2: **no puedes
conectar los viajes con información personal identificable de los usuarios**, lo que impide saber si
un mismo casual hizo varios viajes o si vive en el área de servicio. Esa limitación se declara.

### Puntos de atención por fase

- **Preguntar.** El problema de negocio (los ingresos dependen de las membresías anuales) no es la
  pregunta analítica (cómo difieren los patrones de uso). Escribe las dos, y la decisión que habilita.
- **Preparar.** Doce archivos mensuales que hay que combinar → esto ya justifica elegir Python o SQL
  sobre una hoja de cálculo, y esa justificación es material de portafolio.
- **Procesar.** Duraciones negativas o de cero, viajes de mantenimiento, nombres de estación
  inconsistentes, columnas que cambian de esquema entre meses. Cuenta cada eliminación.
- **Analizar.** Duración media **y mediana** por tipo de usuario (la distribución es muy asimétrica),
  distribución por día de semana, estacionalidad mensual, tipo de bicicleta, estaciones más usadas
  por cada grupo.
- **Compartir.** Titulares con el hallazgo. El ejecutivo detallista va a preguntar por la calidad de
  los datos: prepara esa respuesta.
- **Actuar.** Aquí se separan los portafolios. "Los casuales viajan más los fines de semana" es un
  hallazgo. La recomendación necesita canal, momento, mensaje, métrica de éxito y supuesto.

---

## Brief 2 — Bellabeat: ¿cómo puede una empresa de bienestar jugar con inteligencia?

### Escenario

Eres analista de datos junior en el equipo de marketing de **Bellabeat**, fabricante de productos de
salud enfocados en mujeres. Es una empresa pequeña y exitosa con potencial de crecer en el mercado
global de dispositivos inteligentes. **Urška Sršen**, cofundadora y directora creativa, cree que
analizar datos de uso de dispositivos inteligentes puede revelar oportunidades de crecimiento.

Te piden **enfocarte en uno de los productos de Bellabeat** y analizar datos de dispositivos
inteligentes para entender cómo los consumidores los usan. Los hallazgos guiarán la estrategia de
marketing. Presentarás el análisis al equipo ejecutivo junto con recomendaciones de alto nivel.

### Personajes

| Quién | Rol |
|---|---|
| **Urška Sršen** | Cofundadora y directora creativa |
| **Sando Mur** | Matemático, cofundador, miembro del equipo ejecutivo |
| **Equipo de analítica de marketing** | Tus colegas |

### Productos

- **App Bellabeat** — datos de actividad, sueño, estrés, ciclo menstrual y hábitos de atención plena.
  Se conecta con toda la línea de productos.
- **Leaf** — rastreador clásico de bienestar; se lleva como pulsera, collar o clip. Registra
  actividad, sueño y estrés.
- **Time** — reloj de bienestar con apariencia de reloj clásico. Actividad, sueño y estrés.
- **Spring** — botella de agua que registra la hidratación diaria.
- **Membresía Bellabeat** — suscripción con orientación personalizada 24/7 en nutrición, actividad,
  sueño, salud, belleza y atención plena.

### La tarea

Elige **un** producto y responde: **¿cómo usan los consumidores sus dispositivos inteligentes, y qué
implica eso para el marketing de ese producto?**

La elección del producto es tuya y es una decisión de la fase 1 que hay que justificar por escrito.
Justificarla con los datos disponibles es legítimo — declararlo lo es más.

### Datos

Datos públicos de uso de dispositivos de fitness (tipo FitBit), con registros minuto a minuto de
actividad física, ritmo cardíaco y sueño. Limitaciones importantes que **deben** declararse en la
fase 2 y volver a aparecer en la fase 6:

- **Muestra muy pequeña** — unas decenas de usuarios.
- **Ventana temporal corta** — cerca de dos meses.
- **Sin datos demográficos** — no se sabe el género, y Bellabeat vende a mujeres. Esto es un problema
  de representatividad directo sobre la pregunta de negocio.
- **Muestra por conveniencia** — usuarios que consintieron compartir datos. Sesgo de autoselección.
- Datos de terceros, no de Bellabeat: falla la **O** de ROCCC.

Este caso es, en el fondo, **un ejercicio de honestidad intelectual**. Un análisis que reconoce estas
limitaciones y aun así extrae recomendaciones prudentes demuestra más criterio que uno que las
ignora y concluye con seguridad.

### Puntos de atención por fase

- **Preguntar.** Elegir el producto y justificarlo. Sin eso, las recomendaciones de la fase 6 no
  aterrizan en nada.
- **Preparar.** Aquí está el 60 % del valor del caso: evaluar ROCCC con dureza y declarar cada falla.
- **Procesar.** Varias tablas con granularidades distintas (por minuto, por hora, por día). Unificar
  la granularidad es la decisión de limpieza principal y hay que documentar por qué elegiste una.
- **Analizar.** Segmentar usuarios por nivel de actividad, relación entre pasos y sueño, patrones por
  día de la semana, y **cuántos días registra realmente cada usuario** (muchos no llevan el
  dispositivo todos los días — eso es un hallazgo en sí mismo).
- **Compartir.** Las limitaciones van visibles, no escondidas en un anexo.
- **Actuar.** Recomendaciones con el supuesto explícito y "qué datos adicionales fortalecerían esto"
  bien desarrollado: demográficos, muestra mayor, serie más larga, datos propios de Bellabeat.

---

## Cómo usar estos briefs

1. Copia la plantilla `CASO.md` de `references/plantillas.md`.
2. Pega el brief correspondiente en la sección de contexto.
3. Empieza por `references/01-preguntar.md`. **No saltes la fase 1** porque el brief parezca darte la
   pregunta hecha: traducir el encargo a pregunta analítica, decisión y métricas operativas es
   exactamente el trabajo.
4. Recorre las seis fases, pasando cada puerta de salida.
5. Antes de publicar, `references/criterios-de-calidad.md`.
