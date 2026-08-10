# Anexo — Visualización y Tableau

Detalle operativo de la fase **Compartir**: cómo elegir el tipo de gráfico, cómo construirlo en
Tableau, y cómo verificar diseño y accesibilidad antes de publicar.

`05-compartir.md` cubre el marco (audiencia, método McCandless, filtro de tres partes). Este anexo
es el catálogo y la mecánica.

---

## 1. Selector de gráfico según la forma de la pregunta

Empieza por qué tiene tu dato, no por qué gráfico te gusta.

### Una variable que cambia entre categorías

| Gráfico | Variante | Cuándo |
|---|---|---|
| **Líneas** | Simple | Una sola categoría |
| | Apilado | Varias categorías y quieres compararlas |
| **Columnas** (barras verticales) | Simple | Una categoría |
| | Agrupadas | Varias categorías, comparación directa entre ellas |
| | Apiladas | Varias categorías y el total también importa |
| **Barras horizontales** | Igual que columnas | Etiquetas largas, o valores muy dispares que harían la columna demasiado alta |

### Una variable que cambia en el tiempo

| Gráfico | Cuándo |
|---|---|
| **Líneas** (tiempo en el eje X) | La opción por defecto para tendencias |
| **Líneas apiladas** | Varios elementos o clasificaciones a lo largo del tiempo |
| **Áreas sin apilar** | Los datos no coinciden en el eje X (puntos de tiempo distintos) |
| **Áreas apiladas** | Los datos coinciden en el eje X y el total acumulado importa |

### Tendencia numérica

| Gráfico | Cuándo |
|---|---|
| **Histograma** | Distribución: cuántos casos caen en cada rango de valores |
| **Dispersión** | Relación entre dos variables numéricas |
| **Burbujas** | Igual que dispersión, con una tercera variable codificada en el tamaño |

### Parte y todo

| Gráfico | Cuándo |
|---|---|
| **Circular (pastel)** | Proporciones que suman 100 %. **Solo con 2–3 porciones** |
| **Anillo (dona)** | Igual que el circular, con la misma restricción |
| **Barras apiladas al 100 %** | Más de tres partes: casi siempre mejor que el circular |
| **Treemap** | Muchas categorías con jerarquía |

> Nada en 3D. El volumen distorsiona la percepción del área y no aporta información. Si tu
> herramienta ofrece un pastel 3D, esa opción existe para que no la uses.

### Progreso hacia una meta

| Gráfico | Cuándo |
|---|---|
| **Medidor (gauge)** | Un resultado dentro de un rango permitido |
| **Bala (bullet)** | Resultado contra objetivo, en formato compacto. Superior al medidor |

### Intensidad o frecuencia

| Gráfico | Cuándo |
|---|---|
| **Mapa de calor** | Intensidad por combinación de dos dimensiones (hora × día, por ejemplo) |
| **Tabla resaltada** | Tabla con formato condicional por color: números exactos + patrón visual |
| **Mapa de densidad** | Concentración de puntos en un área geográfica |
| **Mapa de símbolos** | Marcas sobre coordenadas concretas |
| **Mapa coroplético** | Valor por región. **Normaliza siempre** (por población, por área): un mapa de conteos absolutos es un mapa de dónde vive la gente |

### Flujo y relaciones

| Gráfico | Cuándo |
|---|---|
| **Sankey** | Flujo entre estados o categorías |
| **Embudo** | Caída entre etapas sucesivas de un proceso |
| **Burbujas agrupadas** (packed bubble) | Comparar magnitudes sin eje; decorativo más que preciso |
| **Caja y bigotes** | Distribución y atípicos, comparando varios grupos |

---

## 2. Elementos que toda visualización debe tener

Vocabulario del certificado, y checklist a la vez:

- **Titular (headline):** el texto superior. Comunica **el hallazgo**, no el tema.
- **Subtítulo:** añade contexto — periodo, alcance, unidad, fuente.
- **Etiquetas (labels):** identifican valores o describen una escala.
- **Leyenda:** explica qué significa cada elemento. Si puedes usar etiquetas directas, elimínala.
- **Marcas (marks):** los objetos visuales — puntos, líneas, barras.
- **Anotaciones:** señalan el punto concreto que importa. Ahorran un párrafo.
- **Nota de fuente:** al pie. Da credibilidad y permite verificar.

---

## 3. Elementos del arte aplicados al diseño

Los seis que el certificado destaca, con su uso analítico:

| Elemento | Uso correcto | Trampa |
|---|---|---|
| **Línea** | Conectar puntos en el tiempo, dirigir la vista | Líneas de cuadrícula densas que compiten con el dato |
| **Forma** | Codificar categoría **además** del color | Formas decorativas sin significado |
| **Color** | Destacar lo importante; gris para el contexto | Un color distinto por categoría cuando no hace falta |
| **Espacio** | Separar, agrupar, dar respiro | Rellenar todo el espacio disponible |
| **Movimiento** | Solo en visualizaciones dinámicas, con propósito | Animación por defecto en presentaciones |
| **Tamaño** | Codificar magnitud en burbujas y treemaps | Escalar por diámetro en vez de por área: exagera |

### Principios que más impacto tienen

- **Contraste dirigido.** Un color para el protagonista, gris para todo lo demás. Si todo resalta,
  nada resalta.
- **Relación tinta/dato.** Elimina cuadrícula pesada, bordes, fondos, sombras y todo lo tridimensional.
  Cada píxel debe representar dato.
- **Eje desde cero en barras.** Sin excepción: la longitud de la barra *es* el dato. En líneas puedes
  recortar el eje, pero indícalo.
- **Orden con intención.** Por valor, no alfabético, salvo que el orden tenga significado propio
  (meses, etapas de un embudo).
- **Consistencia entre gráficos.** El mismo color significa lo mismo en todo el informe. Cambiar el
  código de color a mitad de una presentación destruye la confianza.
- **Regla de los cinco segundos.** Si la audiencia necesita más de cinco segundos para entender de
  qué habla el gráfico, el gráfico está mal.

---

## 4. Accesibilidad — requisito, no adorno

- **Nunca codifiques información solo con color.** Añade forma, patrón, etiqueta o posición. Alrededor
  del 8 % de los hombres tiene alguna deficiencia en la visión del color.
- **Paletas seguras** para daltonismo (viridis, cividis, o paletas verificadas con un simulador).
- **Contraste de texto suficiente** sobre el fondo.
- **Texto alternativo** descriptivo en cada figura: qué muestra y cuál es el hallazgo, no "gráfico de
  barras".
- **Tamaño de fuente legible en el medio real.** Lo que se lee en tu monitor no se lee en un
  proyector ni en un móvil.
- **Ofrece la tabla de datos** junto al gráfico, o enlázala. Un lector de pantalla no puede leer una
  imagen.
- **Etiquetas directas** en lugar de leyenda: reduce la carga cognitiva para todos.

---

## 5. Tableau: mecánica y vocabulario

Vale la pena solo si el caso justifica interactividad o si quieres demostrar la herramienta. Para un
gráfico estático en un README, matplotlib o la hoja de cálculo bastan.

**Conceptos:**

- **Dimensiones** (azul, discretas) → categorías. **Medidas** (verde, continuas) → números que se
  agregan.
- **Marks card:** controla color, tamaño, etiqueta, detalle y tooltip de cada marca. Es donde se
  hace el 80 % del diseño.
- **Show Me:** sugiere tipos de gráfico según lo que arrastraste. Útil para explorar, **peligroso
  como decisión final**: elige por objetivo, no por lo que Tableau propone primero.
- **Campo calculado:** columnas derivadas dentro de Tableau. Documéntalas como cualquier otra
  transformación de la fase 3.
- **Data blending:** combina datos de fuentes distintas a nivel de agregado. Distinto de un JOIN, que
  combina a nivel de fila. Confundirlos produce números que no cuadran.
- **Dashboard:** varias vistas juntas, con filtros y acciones que las conectan. Monitorea datos que
  se actualizan.
- **Story:** secuencia de vistas con narrativa. Es la opción adecuada para un caso de estudio.
- **Tooltip:** el detalle que aparece al pasar el cursor. Aprovéchalo para poner el número exacto y
  aligerar el gráfico.

**Publicar:** Tableau Public es gratuito y enlazable desde el portafolio. Cualquier cosa que subas
ahí **es pública**. Verifica que no haya datos sensibles antes de publicar.

**Visualizaciones dinámicas:** interactivas o que cambian solas. Justifícalas — si el hallazgo se
entiende igual en una imagen estática, la interactividad es fricción para el lector.

---

## 6. Del gráfico a la historia

Una historia de datos tiene tres partes: **personajes** (a quién afecta), **escenario** (contexto y
conflicto) y **trama** (qué muestran los datos y qué implica).

- **Spotlighting:** recorre todos tus hallazgos y marca los tres a cinco que sostienen el argumento.
  Solo esos se presentan. El resto va a anexo o se descarta.
- Cada gráfico defiende **un** mensaje. Dos mensajes en un gráfico son cero mensajes.
- La secuencia de gráficos debe construir el argumento: cada uno introduce lógicamente al siguiente.
- El gráfico debe leerse sin ti. Si necesita tu narración para entenderse, no sirve en un README.

---

## Puerta de salida específica de visualización

- [ ] Tipo de gráfico elegido por objetivo, con justificación escrita.
- [ ] Titular de cada figura enuncia el hallazgo.
- [ ] Subtítulo con periodo, alcance y unidad.
- [ ] Nota de fuente al pie.
- [ ] Eje desde cero en todas las barras.
- [ ] Un color protagonista, resto en gris.
- [ ] Ningún elemento 3D, ninguna sombra, cuadrícula mínima.
- [ ] Ordenado por valor salvo que el orden tenga significado.
- [ ] Información nunca codificada solo con color.
- [ ] Texto alternativo escrito para cada figura.
- [ ] Legible en el medio real de consumo.
- [ ] Solo se presentan los gráficos que sostienen el argumento.

## Errores comunes

- Título que nombra el tema (`"Duración por tipo de usuario"`) en vez del hallazgo.
- Gráfico circular con ocho porciones.
- Eje truncado en barras, que exagera diferencias reales pero pequeñas.
- Mapa coroplético de conteos absolutos sin normalizar.
- Aceptar lo que sugiere *Show Me* sin preguntarse si responde la pregunta.
- Paleta de arcoíris para una variable ordenada: no tiene orden perceptual.
- Escalar burbujas por diámetro en lugar de por área.
- Mostrar los quince gráficos producidos en vez de los cuatro que argumentan.
