# Anexo — Hojas de cálculo

Referencia operativa para las fases **Procesar** y **Analizar** cuando la herramienta es Excel o
Google Sheets. Aplica también cuando la hoja es solo el paso de exploración inicial antes de pasar a
SQL o Python.

---

## 1. Cuándo la hoja de cálculo es la decisión correcta

**Sí:** menos de ~100.000 filas, exploración rápida, revisión visual de anomalías, entregable que la
parte interesada quiere poder abrir y tocar.

**No:** el proceso se repetirá cada mes, hay varios archivos que combinar, el volumen es alto, o el
caso necesita auditoría estricta de cada transformación. Ahí pierde frente a SQL y Python porque el
registro de qué hiciste es frágil.

En un caso de portafolio, justifica la elección por escrito. Elegir la hoja porque el dataset son
5.000 filas y el cliente la va a revisar a mano es una decisión sólida. Elegirla por costumbre no.

---

## 2. Higiene del archivo antes de empezar

Ocho prácticas que previenen la mayoría de los errores:

1. **Una pestaña con los datos crudos, intacta.** Otra pestaña para trabajar. Nunca se limpia sobre
   el crudo.
2. **Congela la fila de encabezados** para saber siempre qué columna estás mirando al desplazarte.
3. **Filtra** para reducir el ruido visual en lugar de borrar filas.
4. **Toda fórmula empieza con `=`.** Toda apertura de paréntesis tiene su cierre.
5. **Multiplicar es `*`, no `x`.**
6. **Fuente legible y bordes en blanco:** trabajar sobre una cuadrícula visualmente limpia reduce
   errores de lectura de celda.
7. **Validación de datos** en las columnas de entrada: evita que el error entre, en lugar de tener
   que cazarlo después.
8. **Formato condicional** para que las anomalías se vean solas.

---

## 3. Errores y cómo se arreglan

| Error | Qué significa | Causa típica | Arreglo |
|---|---|---|---|
| `#DIV/0!` | División por cero o por celda vacía | `=B2/B3` con `B3 = 0` | Envolver en `IFERROR`: `=IFERROR(C4/B4*100, "No aplica")` |
| `#ERROR!` (solo Sheets) | Error de análisis sintáctico | Rangos sin coma: `=SUM(B2:B6 C2:C6)` | Separar con coma: `=SUM(B2:B6,C2:C6)` |
| `#N/A` | La fórmula no encuentra el dato | `BUSCARV` sobre un valor que no está (`Almendra` vs `Almendras`) | Corregir el valor buscado o la tabla de búsqueda |
| `#NAME?` | No reconoce el nombre de la función | Tipeo: `VLOOOKUP` | Revisar ortografía; usar el autocompletado |
| `#NUM!` | No puede ejecutar el cálculo | `DATEDIF` con fecha inicial posterior a la final; número fuera de rango | Revisar el orden y el rango de los argumentos |
| `#REF!` | Referencia a una celda que ya no existe | Se borró una fila o columna usada en la fórmula | Reescribir la fórmula con las referencias vivas |
| `#VALUE!` | Problema general con la fórmula o las celdas | Texto donde se espera número; espacios ocultos | Revisar tipos de las celdas referenciadas |

### Truco: encontrar todos los errores de una hoja de golpe

Formato condicional con fórmula personalizada `=ISERROR(A1)` aplicada a toda la hoja, con relleno
amarillo. Los errores aparecen resaltados y se corrigen en lote.

- **Excel:** seleccionar todo → Inicio → Formato condicional → Nueva regla → *Usar una fórmula* →
  `=ISERROR(A1)` → Formato → Relleno amarillo.
- **Google Sheets:** seleccionar todo → Formato → Formato condicional → *La fórmula personalizada
  es* → `=ISERROR(A1)` → color de relleno → Listo.

---

## 4. Funciones de limpieza (fase 3)

| Necesidad | Función | Nota |
|---|---|---|
| Quitar espacios sobrantes | `ESPACIOS` / `TRIM` | Quita los del inicio, del final y los dobles internos |
| Quitar caracteres no imprimibles | `LIMPIAR` / `CLEAN` | Típico tras exportar de un sistema |
| Unificar mayúsculas | `MAYUSC`, `MINUSC`, `NOMPROPIO` | Estandariza categorías |
| Separar un campo | Datos → Dividir texto en columnas | `nombre completo` → `nombre`, `apellido` |
| Unir campos | `CONCATENAR` / `&` | — |
| Buscar y traer un dato | `BUSCARV` / `VLOOKUP` | Falla si la clave no está exacta |
| Igual pero robusto | `INDICE` + `COINCIDIR` | No se rompe al insertar columnas; preferible |
| Longitud de una cadena | `LARGO` / `LEN` | Detecta códigos mal formados |
| Extraer parte de un texto | `IZQUIERDA`, `DERECHA`, `EXTRAE` / `MID` | — |
| Eliminar duplicados | Datos → Quitar duplicados | **Cuenta cuántos elimina y anótalo** |
| Buscar y reemplazar | Ctrl+H | Con "coincidir mayúsculas" activado si importa |
| Atrapar errores | `SI.ERROR` / `IFERROR` | No lo uses para tapar un error que no entiendes |

**Advertencia sobre `BUSCARV`:** devuelve `#N/A` cuando no encuentra la clave. Ese `#N/A` es
información valiosa (te dice cuántos registros no cruzaron). Envolverlo en `SI.ERROR` desde el
principio esconde el problema. Primero cuenta los `#N/A`, entiende por qué, y solo entonces decide
qué hacer con ellos.

---

## 5. Funciones de análisis (fase 4)

| Objetivo | Funciones |
|---|---|
| Estadística descriptiva | `SUMA`, `PROMEDIO`, `MEDIANA`, `MIN`, `MAX`, `DESVEST`, `CONTAR`, `CONTARA` |
| Conteo condicional | `CONTAR.SI`, `CONTAR.SI.CONJUNTO` |
| Suma condicional | `SUMAR.SI`, `SUMAR.SI.CONJUNTO` |
| Promedio condicional | `PROMEDIO.SI`, `PROMEDIO.SI.CONJUNTO` |
| Multiplicar y sumar arreglos | `SUMAPRODUCTO` |
| Trabajo con fechas | `FECHA`, `DIASEM`, `DATEDIF`, `HOY` |
| Resto de una división | operador `%` (módulo) |
| Redondeo | `REDONDEAR` |

**Regla de la fase 4: siempre mediana junto a la media.** Si difieren mucho, la distribución es
asimétrica y reportar solo la media distorsiona la conclusión.

### Tablas dinámicas

Son la herramienta central del análisis en hoja de cálculo. Estructura mental:

- **Filas:** la dimensión por la que segmentas (tipo de usuario, mes, categoría).
- **Columnas:** la segunda dimensión, si la hay.
- **Valores:** la métrica y su función de resumen (suma, promedio, cuenta).
- **Filtros:** el subconjunto sobre el que trabajas.

Cada tabla dinámica que sostenga un hallazgo debe quedar registrada: qué dimensión, qué métrica, qué
filtro. Es el equivalente en hoja de cálculo a publicar la consulta SQL.

Un **gráfico dinámico** hereda los campos de su tabla dinámica y se actualiza con ella.

### Ordenar: la trampa clásica

Distingue siempre:

- **Ordenar rango:** solo se mueve la selección. Si seleccionaste una columna y ordenas, esa columna
  se reordena y **las demás no**. El dataset queda corrupto y no hay ningún mensaje de error.
- **Ordenar hoja:** todas las filas se mueven juntas, manteniendo la correspondencia.

Salvo que sepas exactamente por qué, quieres ordenar la hoja. Y antes de ordenar, guarda una copia.

---

## 6. Verificación antes de cerrar la fase

- Reconciliación de conteos: filas iniciales − eliminadas = filas finales, exacto.
- Barre la hoja con `=ISERROR()` y confirma que no queda ningún error.
- Revisa la lista de valores únicos de cada categórica: debe ser el conjunto esperado, sin sorpresas.
- Comprueba que los rangos numéricos son plausibles (mínimos y máximos).
- Verifica que ninguna fórmula quedó apuntando a la pestaña de crudos por accidente.

---

## Puerta de salida específica de hojas de cálculo

- [ ] Pestaña de datos crudos intacta y separada de la de trabajo.
- [ ] Ninguna celda con error (`ISERROR` barrido y limpio).
- [ ] Cada eliminación de duplicados tiene su conteo registrado.
- [ ] Cada tabla dinámica que sostiene un hallazgo está documentada (dimensión, métrica, filtro).
- [ ] Ningún ordenamiento se hizo sobre un rango parcial.
- [ ] Los `#N/A` de las búsquedas fueron contados y explicados, no tapados con `SI.ERROR`.
- [ ] Las fórmulas clave están documentadas en la bitácora, no solo dentro de las celdas.

## Errores comunes

- Limpiar sobre la pestaña de datos crudos.
- Ordenar un rango en lugar de la hoja y desalinear todas las filas.
- Envolver todo en `SI.ERROR` desde el inicio y perder la señal de que algo no cruza.
- Reportar promedios sin mirar la mediana.
- Entregar el archivo sin una hoja que explique qué contiene cada pestaña.
- Confiar en que "se ve bien" en pantalla: 200.000 filas no se revisan visualmente.
