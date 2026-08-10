# Fase 2 — Preparar

**Objetivo:** conseguir datos que realmente respondan la pregunta, verificar que se puede confiar
en ellos y dejarlos organizados de forma reproducible.

**Entregable:** una descripción de todas las fuentes de datos usadas.

---

## 1. Decide qué datos necesitas antes de buscarlos

Escribe la lista ideal de campos que la pregunta exige, con granularidad y periodo. Recién entonces
busca. Al revés, terminas justificando el dataset que encontraste.

Ejes para clasificar lo que consigas:

- **Origen:** primera parte (recolectada por la propia organización), segunda parte (recolectada por
  otro y compartida directamente), tercera parte (agregador o vendedor). La confianza cae en ese orden.
- **Ubicación:** interna o externa.
- **Estructura:** estructurada (tablas), semiestructurada, no estructurada (texto, imágenes, audio).
- **Tipo:** cuantitativa (discreta o continua) o cualitativa (nominal u ordinal).
- **Corte temporal:** transversal (un punto en el tiempo) o longitudinal (mismos sujetos a lo largo
  del tiempo). Las preguntas causales casi siempre necesitan lo segundo.

## 2. Verifica la credibilidad: ROCCC

| Letra | Criterio | Qué revisar |
|---|---|---|
| **R** | Confiable (*Reliable*) | Preciso, completo, imparcial. ¿Quién lo recolectó y con qué método? |
| **O** | Original (*Original*) | ¿Es la fuente primaria o una copia de una copia? Rastrea hasta el origen. |
| **C** | Completo (*Comprehensive*) | ¿Contiene todos los campos que la pregunta necesita? |
| **C** | Actual (*Current*) | ¿La ventana temporal sigue siendo relevante para la decisión? |
| **C** | Citado (*Cited*) | ¿Está documentado quién, cuándo, cómo y bajo qué licencia? |

Un dato que falla dos o más letras no se descarta automáticamente, pero **la limitación se declara
por escrito** y se explica cómo afecta las conclusiones.

## 3. Busca el sesgo activamente

- **Sesgo de muestreo:** la muestra no representa a la población. Es el más frecuente y el más caro.
- **Sesgo del observador:** el método de medición varía según quién mide.
- **Sesgo de interpretación:** hay más de una lectura y se elige la conveniente.
- **Sesgo de confirmación:** se buscan datos que respalden una creencia previa.
- **Sesgo de supervivencia:** solo se observa lo que llegó al dataset. Pregunta siempre *quién no
  está aquí y por qué*.

Contramedida práctica: escribe, antes de analizar, qué resultado esperas. Si el análisis lo confirma
demasiado limpiamente, revísalo con más dureza, no con menos.

## 4. Muestreo y suficiencia

Cuando no trabajes con la población completa, deja registrado:

- **Población** y **muestra** con su método de selección (aleatoria, estratificada, por conveniencia).
- **Tamaño de muestra**, **margen de error**, **nivel de confianza** e **intervalo de confianza**.
- Si es muestra por conveniencia, dilo. No es descalificante, es información.

Nota de criterio: una muestra grande pero sesgada es peor que una pequeña y representativa, porque
da falsa seguridad.

## 5. Licencia, privacidad, seguridad y accesibilidad

Cuatro preguntas obligatorias por fuente:

- **Licencia:** ¿qué permite exactamente? (CC0, CC BY, uso no comercial, propietaria). Cítala.
- **Privacidad:** ¿hay información personal identificable? Si la hay, anonimiza o agrega. Nunca
  publiques datos personales en un repositorio de portafolio.
- **Seguridad:** ¿dónde vive el dato, quién accede, se encripta?
- **Accesibilidad:** ¿puede otra persona reproducir tu acceso a la fuente? Si no, el caso no es
  reproducible.

## 6. Organiza y documenta

- Copia inmutable del crudo en `datos/crudos/`, marcada como solo lectura.
- Convención de nombres consistente y descriptiva: `origen_tema_periodo_version.csv`.
- Sin espacios ni acentos en nombres de archivo; fechas en `AAAA-MM-DD` para que ordenen bien.
- Registra los **metadatos**: descriptivos (qué es), estructurales (cómo se organiza y relaciona),
  administrativos (origen, licencia, fecha de descarga, autor).
- Un **diccionario de datos**: por columna, nombre, tipo, unidad, valores permitidos, significado.

Rellena una ficha por fuente usando la plantilla de `plantillas.md`.

## 7. Prueba de integridad inicial

Antes de declarar la fase cerrada:

- Conteo de filas y columnas; ¿coincide con lo que la fuente declara?
- Rango de fechas real vs esperado.
- Valores nulos por columna.
- Cardinalidad de las claves; ¿hay duplicados donde debería haber unicidad?
- Valores mínimos y máximos por campo numérico: los imposibles saltan aquí.

---

## Puerta de salida

- [ ] Cada fuente tiene su ficha completa (origen, licencia, periodo, granularidad, acceso).
- [ ] ROCCC evaluado por fuente, con las fallas declaradas.
- [ ] Sesgos potenciales identificados por escrito.
- [ ] Licencia, privacidad, seguridad y accesibilidad resueltas.
- [ ] Diccionario de datos escrito.
- [ ] Copia inmutable del crudo guardada, con convención de nombres.
- [ ] Prueba de integridad inicial ejecutada, con sus resultados anotados.
- [ ] Confirmado que estos datos **sí** pueden responder la pregunta de la fase 1. Si no, se vuelve
      a la fase 1.

## Errores comunes

- Descargar y empezar a limpiar sin leer la documentación de la fuente.
- No registrar la fecha de descarga: meses después nadie sabe qué versión se usó.
- Suponer que "público" equivale a "libre de usar y publicar".
- Trabajar directamente sobre el archivo crudo.
- Descubrir en la fase 4 que falta la columna que la pregunta necesitaba.
