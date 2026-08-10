# Fase 4 — Analizar

**Objetivo:** encontrar patrones, relaciones y tendencias que respondan la pregunta de la fase 1, y
verificar que son reales y no artefactos.

**Entregable:** un resumen del análisis.

---

## 1. Los cuatro pasos del análisis

1. **Organizar** — ordenar y filtrar para que los datos sean navegables.
2. **Formatear y ajustar** — tipos, unidades y columnas derivadas que el análisis necesita.
3. **Obtener entrada** — cálculos, agregaciones, tablas dinámicas, consultas.
4. **Transformar** — convertir los resultados en información interpretable.

## 2. Organizar

- **Ordenar:** define el criterio antes de ordenar. En hojas de cálculo, distingue ordenar un rango
  (solo esa selección) de ordenar la hoja (todas las filas se mueven juntas). Confundirlos
  desalinea filas y corrompe el dataset silenciosamente.
- **Filtrar:** aísla subconjuntos para verlos por separado. Filtrar no es lo mismo que segmentar
  para el análisis — documenta cuál estás haciendo.
- **Columnas derivadas:** día de la semana, duración, mes, categoría agrupada, bandera booleana.
  Se crean aquí y se documentan igual que una limpieza.

## 3. Calcular

**Hojas de cálculo:** funciones de agregación (`SUMA`, `PROMEDIO`, `MEDIANA`, `CONTAR.SI`,
`SUMAR.SI.CONJUNTO`), tablas dinámicas para agregar por dimensión, `BUSCARV`/`INDICE`+`COINCIDIR`
para combinar tablas.

**SQL:** funciones de agregación con `GROUP BY`; uniones (`INNER`, `LEFT`, `RIGHT`, `FULL OUTER`)
sabiendo cuál corresponde y por qué; subconsultas y CTEs (`WITH`) para mantener legibilidad;
funciones de ventana para rankings, acumulados y comparaciones contra el grupo.

**Python:** `groupby().agg()`, `merge()`, `pivot_table()`, `describe()`, `value_counts()`,
`corr()`, `resample()` para series de tiempo.

## 4. Qué buscar

- **Estadística descriptiva primero, siempre:** conteo, media, mediana, desviación, mínimo, máximo,
  percentiles. Si la media y la mediana difieren mucho, hay asimetría y la media engaña.
- **Comparación entre segmentos:** el corazón de la mayoría de las preguntas de negocio. Compara el
  grupo de interés contra una línea base clara.
- **Evolución temporal:** tendencia, estacionalidad, ciclos, quiebres. Separa señal de ruido.
- **Distribución, no solo promedios:** un promedio esconde bimodalidades. Míralas.
- **Relaciones entre variables:** correlación como punto de partida. **Correlación no es
  causalidad** — escríbelo en el informe cada vez que muestres una.
- **Anomalías:** lo que no encaja suele ser el hallazgo más valioso, o el error más grande.

## 5. Verifica antes de creer

Antes de dar un resultado por bueno:

- **Prueba de sensatez:** ¿el orden de magnitud es plausible? ¿el total cuadra con una fuente
  independiente?
- **Recálculo por otra vía:** obtén la misma cifra con un método distinto. Si no coincide, hay un bug.
- **Revisa denominadores y filtros:** la causa nº 1 de resultados espectaculares y falsos.
- **Revisa el sesgo de interpretación:** ¿hay otra lectura del mismo resultado? Escríbela y
  descártala con evidencia, no con preferencia.
- **Efecto de tamaño, no solo dirección:** una diferencia real pero de 0.3 % no sostiene una
  recomendación.
- **Cuidado con la agregación:** un patrón puede invertirse al desagregar por subgrupo. Revisa
  siempre al menos un nivel más abajo.

## 6. Documenta los cálculos

Por cada hallazgo registra: la pregunta que responde, el cálculo exacto (fórmula, consulta o celda
de código), el resultado con su unidad, el subconjunto usado y la interpretación en una frase.
Sin esto, la fase 5 se construye sobre memoria.

---

## Puerta de salida

- [ ] Estadística descriptiva completa y revisada.
- [ ] Cada pregunta de la fase 1 tiene una respuesta basada en un cálculo concreto.
- [ ] Todos los cálculos documentados y reproducibles.
- [ ] Cada hallazgo pasó prueba de sensatez y recálculo por vía alterna.
- [ ] Efectos cuantificados, no solo direccionales.
- [ ] Interpretaciones alternativas consideradas y descartadas con evidencia.
- [ ] Lo que los datos **no** pueden responder está escrito como limitación.
- [ ] Ninguna afirmación causal apoyada solo en correlación.

## Errores comunes

- Reportar promedios sobre distribuciones asimétricas.
- Comparar segmentos sin una línea base definida.
- Encontrar el patrón esperado y dejar de buscar ahí mismo.
- Perder filas silenciosamente en una unión mal elegida.
- Confundir "no encontré diferencia" con "no hay diferencia" cuando la muestra es pequeña.
