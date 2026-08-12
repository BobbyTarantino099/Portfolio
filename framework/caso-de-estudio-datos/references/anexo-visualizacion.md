# Anexo — Visualización

Detalle operativo de la fase **Compartir**: cómo elegir el tipo de gráfico, qué identidad visual
aplicarle, y cómo verificar diseño y accesibilidad antes de publicar.

`05-compartir.md` cubre el marco (audiencia, método McCandless, filtro de tres partes). Este anexo
es el catálogo, la identidad y la mecánica.

Las secciones **1 a 4 son buenas prácticas**: evitan que el gráfico esté mal. Las secciones **5 a
8 son la identidad**: consiguen que el gráfico se vea propio. Son cosas distintas y hacen falta
las dos.

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

## 5. La identidad visual

Las secciones 1 a 4 son buenas prácticas: las cumple cualquiera. Lo que hace que una figura se
reconozca como tuya antes de leer el titular es otra cosa, y es lo que define esta sección.

**El problema que resuelve.** Un gráfico puede cumplir todos los principios —titular con el
hallazgo, un color protagonista, gris de contexto, nota de fuente— y aun así salir con aspecto de
matplotlib por defecto. Cumplir los principios evita que el gráfico esté mal; no consigue que se
vea propio.

### La composición, idéntica en toda figura

```
Titular              ~18 pt, peso 700, negro casi puro, alineado a la izquierda
Subtítulo            ~12 pt, gris medio — define la métrica y el alcance
Línea de periodo     ~9 pt, versalitas, gris claro — opcional
─────────────────────────────────────────────
[ el gráfico, sin marco ]
─────────────────────────────────────────────
Fuente + nota        ~8 pt, gris claro, al pie izquierda
Firma                monograma, al pie derecha
```

El salto de tamaño y de color entre los tres niveles de cabecera es deliberado y **más agresivo de
lo que parece natural**. Un titular apenas mayor que el subtítulo no jerarquiza nada.

**El aire entre niveles se mide en puntos, no en fracción del lienzo.** Es la regla menos obvia de
esta sección y la que más rompe cuando se ignora: la tipografía tiene tamaño absoluto, así que un
espaciado expresado como porcentaje de la altura de la figura se aprieta al bajar el lienzo y se
desparrama al subirlo. El mismo diseño que respira a 6,8 pulgadas de alto **colisiona a 6,2**, y
el fallo no aparece hasta que alguien cambia un `figsize`.

Corolario práctico: el alto de cada bloque de texto se **mide** del texto ya compuesto
(`get_window_extent`), no se estima contando caracteres. `textwrap` ya sabe cuántas líneas salieron
y el renderizador sabe cuánto ocupan; estimarlo es elegir equivocarse con titulares que reparten
mal las palabras.

### La paleta

Un acento único y fuerte, gris neutro para todo lo demás, un cálido secundario para el otro lado
de una comparación, y una rampa secuencial de un solo tono para intensidad. Todo validado sobre
fondo blanco antes de fijarlo — **la paleta se computa, no se elige a ojo**.

El acento debe ser el mismo color que usa el sitio donde se publica la figura. Si el gráfico y la
página hablan idiomas distintos, la figura parece pegada.

### La firma

Toda figura lleva monograma. Ninguna sale sin marca, ni siquiera las de trabajo interno: es lo que
convierte una captura reenviada en una figura atribuible. Se dibuja **con texto, no con imagen**,
para no arrastrar un archivo por caso.

### Lo que no se puede copiar de las referencias deportivas

Las visualizaciones de Sportradar, Synergy o Sportico usan **logos, fotos y escudos como marcas**
en lugar de puntos y barras. Es su rasgo más reconocible y **no transfiere** a datos sin
iconografía —géneros de un catálogo, franjas de precio, cohortes—. Perseguirlo es perder el
tiempo. Sin logos, la identidad se sostiene en cuatro sitios, y son justo los que el módulo
garantiza por defecto:

1. El bloque de cabecera, con su salto tipográfico.
2. La firma, presente en toda figura.
3. La anotación directiva: llaves, flechas, etiquetas de cuadrante, texto dentro de las bandas.
4. El tratamiento del número protagonista: grande, en el acento, o dentro de una celda codificada.

---

## 6. La tabla como figura de pleno derecho

**Cuando el número exacto importa, una tabla bien compuesta gana a cualquier gráfico.** No es el
premio de consolación de quien no supo elegir una forma: es la forma correcta cuando el lector
necesita leer valores, no estimarlos.

Un mapa de calor obliga a leer el color y adivinar el número. Una tabla-matriz muestra el número y
usa el color como refuerzo. Casi siempre es mejor cambio.

**Anatomía:**

- Cabecera de columnas en versalitas pequeñas y negrita, con una regla debajo.
- Filas altas, con aire. Separadores finísimos o ninguno.
- **Columna de entidad a dos niveles:** etiqueta principal en negrita, secundaria debajo en gris
  más pequeño y en versalitas (el `n`, la fecha, la categoría padre).
- Columnas numéricas alineadas a la derecha, con cifras tabulares para que los dígitos cuadren.
- **La columna clave va codificada:** celda con degradado, píldora de color, o cifra mucho mayor y
  en el acento. Es lo único que separa una tabla-figura de un volcado de datos.

Con celdas codificadas, el texto cambia a blanco a partir del escalón donde el fondo se oscurece.
Comprobarlo, no suponerlo.

---

## 7. Catálogo de formas que la sección 1 no cubre

| Forma | Cuándo usarla |
|---|---|
| **Dumbbell** | Dos estados por categoría. Muestra la diferencia **como distancia**, que es lo que suele decir el hallazgo. Sustituye a las barras agrupadas casi siempre |
| **Slope** | Dos momentos y lo que importa es el cambio de posición, no la magnitud |
| **Small multiples** | El mismo gráfico repetido por categoría. La forma natural de un control: el patrón se ve repetirse |
| **Lollipop** | Alternativa a barras cuando la masa de la barra es ruido y solo el extremo aporta |
| **Dispersión con cuadrantes anotados** | Dos ejes con significado; las esquinas se etiquetan con el nombre del perfil, no con coordenadas |
| **Barras apiladas al 100 % con el total al final** | Composición y magnitud a la vez, sin recurrir a un doble eje |
| **Tabla-matriz con celdas codificadas** | Sección 6 |

**Barras agrupadas de dos series es la elección por defecto que casi nunca es la mejor.** Obliga a
comparar dos longitudes que arrancan de puntos distintos. Si las series son dos, probablemente sea
un dumbbell.

---

## 8. El módulo `estilo.py`

Está en `assets/estilo.py`. **Se copia a `notebooks/` del caso**, no se importa desde el
framework: así el repo del caso es reproducible por sí solo, que es el punto de la capa L3.

Convierte "acordarse de doce reglas" en llamar a tres funciones:

| Función | Qué hace |
|---|---|
| `aplicar()` | `rcParams`: tipografía, tamaños, sin marco superior ni derecho, cuadrícula tenue |
| `figura(titular, subtitulo, periodo, fuente, nota)` | Devuelve `fig, ax` con cabecera, nota de fuente y firma ya compuestos |
| `destacar(categorias, protagonistas)` | Lista de colores para el contraste dirigido |
| `leyenda(ax)` | Leyenda enmarcada, colocada en el hueco más libre de datos |
| `anotar(ax, texto, xy, xytexto)` | Anotación con flecha en el estilo de la identidad |
| `dumbbell(ax, categorias, desde, hasta)` | La forma de la sección 7 |
| `tabla_matriz(...)` y `tabla_ranking(...)` | Las tablas-figura de la sección 6 |
| `guardar(fig, ruta)` | dpi uniforme |

### La leyenda va donde no hay datos

**Nunca se fija a mano.** `loc="lower right"` funciona hasta que los datos cambian de forma; así
es como una leyenda acabó metida entre las barras del primer grupo, ilegible y sin sentido.
`leyenda()` usa `loc="best"`, que evalúa el solapamiento real con las marcas dibujadas y elige.

Dos detalles que la convierten en bloque en vez de texto flotante: **relleno opaco** y borde fino.
El relleno importa tanto como el borde — es lo que la despega de la cuadrícula.

Y el caso que `best` no puede resolver solo: **cuando no hay ningún hueco**. Con barras desde cero
que llenan el panel, las nueve anclas están ocupadas y `best` devuelve la menos mala, que sigue
pisando datos. Ahí `leyenda()` abre sitio subiendo el techo del eje y la recoloca —ampliar el eje
sin recolocar no sirve, porque `best` ya eligió y no se reevalúa solo—. La base en cero no se
toca: solo se añade aire arriba, así que no distorsiona nada.

**Tres cosas que el módulo resuelve y conviene no deshacer:**

- `guardar()` **no usa `bbox_inches='tight'`**. La cabecera y la firma viven fuera de los ejes; el
  recorte automático se los come.
- El margen inferior no baja de 0.16. Por debajo de eso el rótulo del eje X se solapa con la nota
  de fuente cuando la nota ocupa dos líneas.
- El ritmo vertical vive en las constantes `GAP_*`, en puntos. Tocar esos números cambia el
  espaciado de **todas** las figuras a la vez: es lo que las hace parecer una familia en vez de
  cuatro gráficos con el mismo color.

Después de generar, **abrir las figuras y mirarlas**. El módulo garantiza la composición, no que
una anotación no cruce una etiqueta vecina. Eso solo se ve mirando.

---

## 9. Otras herramientas

**Tableau / Power BI.** Valen la pena si el caso justifica interactividad real o si quieres
demostrar la herramienta. Para una figura estática en un README o en una página, matplotlib basta
y además queda versionada como código.

Dos trampas que sí conviene recordar: *Show Me* sugiere gráficos según lo que arrastraste —útil
para explorar, **peligroso como decisión final**—, y el *data blending* combina a nivel de
agregado mientras que un JOIN combina a nivel de fila; confundirlos produce números que no cuadran.

Lo que subas a Tableau Public **es público**. Verifica que no haya datos sensibles antes.

**Interactividad:** justifícala. Si el hallazgo se entiende igual en una imagen estática, la
interactividad es fricción para el lector.

---

## 10. Del gráfico a la historia

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
- [ ] Composición de la sección 5: cabecera de tres niveles, nota de fuente y firma.
- [ ] Paleta validada sobre el fondo real, no elegida a ojo.
- [ ] Forma revisada contra el catálogo de la sección 7 antes de aceptar la obvia.
- [ ] Figuras abiertas y miradas: ninguna anotación cruza una etiqueta vecina.
- [ ] La cabecera tiene aire entre sus tres niveles, y ninguna leyenda pisa los datos.
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
- Barras agrupadas de dos series donde el hallazgo es una diferencia: eso es un dumbbell.
- Mapa de calor donde el lector necesita el número exacto: eso es una tabla-matriz.
- Dar la figura por buena porque el script no dio error, sin abrir el PNG.
- Espaciar la cabecera en fracciones del lienzo: funciona a un tamaño y colisiona a otro.
- Fijar la leyenda a una esquina y no volver a mirarla cuando los datos cambian de forma.
- Paleta de arcoíris para una variable ordenada: no tiene orden perceptual.
- Escalar burbujas por diámetro en lugar de por área.
- Mostrar los quince gráficos producidos en vez de los cuatro que argumentan.
