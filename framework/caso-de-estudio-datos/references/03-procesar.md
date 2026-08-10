# Fase 3 — Procesar

**Objetivo:** dejar los datos limpios, íntegros y listos para analizar, con un registro que permita
a otra persona reproducir cada transformación.

**Entregable:** la bitácora de limpieza y manipulación de datos.

Esta es la fase que más se subestima y la que más credibilidad aporta en un portafolio. La limpieza
sin documentar es indistinguible de la magia.

---

## 1. Elige la herramienta con criterio, no por costumbre

| Herramienta | Cuándo conviene | Cuándo no |
|---|---|---|
| Hoja de cálculo | < ~100k filas, exploración rápida, revisión visual | Repetible, volumen alto, auditoría estricta |
| SQL | Datos ya en base de datos, uniones entre tablas, volumen alto | Transformaciones muy iterativas o estadística compleja |
| Python (pandas) | Repetibilidad, volumen alto, lógica compleja, todo en un notebook | Cuando quien revisa no lee código |

Justifica la elección por escrito. "Elegí Python porque el proceso debía ser reproducible sobre 12
archivos mensuales" es una frase que un entrevistador valora.

## 2. Protege la integridad de los datos

La **integridad** es la exactitud, completitud, consistencia y confiabilidad del dato a lo largo de
su ciclo de vida. Se compromete en cuatro momentos:

- **Replicación:** copias que se desincronizan.
- **Transferencia:** interrupciones o truncamientos al mover datos.
- **Manipulación:** transformaciones que alteran el significado sin querer.
- **Corrupción:** fallos de disco, virus, exportaciones mal codificadas.

Además evalúa la **suficiencia**: ¿hay datos de un solo periodo cuando la pregunta es de tendencia?
¿La muestra representa a la población? ¿Se está usando un campo como proxy de otro sin declararlo?

## 3. Identifica y corrige datos sucios

| Tipo | Síntoma | Corrección |
|---|---|---|
| Duplicados | La misma entidad más de una vez | Definir la clave e eliminar, contando cuántos |
| Desactualizados | Reemplazados por una versión más nueva | Actualizar desde la fuente o recortar el periodo |
| Incompletos | Campos críticos vacíos | Imputar (y declararlo) o excluir (y contarlo) |
| Incorrectos | Valores válidos en formato pero imposibles | Reglas de negocio: duración negativa, edad de 300 |
| Inconsistentes | El mismo hecho representado de varias formas | Estandarizar categorías, unidades y formatos |

Errores concretos a buscar siempre:

- Espacios al inicio/final y dobles espacios internos.
- Mayúsculas y minúsculas inconsistentes en categorías.
- Errores de tipeo y variantes de la misma categoría (`Bogotá`, `bogota`, `BOGOTA D.C.`).
- Tipos mal asignados: números guardados como texto, fechas como cadenas.
- Formatos de fecha mezclados (`DD/MM/AAAA` vs `MM/DD/AAAA`) — silencioso y devastador.
- Unidades mezcladas en una misma columna.
- Problemas de codificación (acentos rotos → revisar UTF-8).
- Valores atípicos: **no se eliminan por defecto**. Se investigan, y la decisión se justifica.

## 4. Técnicas por herramienta

**Hoja de cálculo:** `TRIM`, `CLEAN`, quitar duplicados, dividir texto en columnas, `CONCATENAR`,
`BUSCARV`/`INDICE`+`COINCIDIR`, buscar y reemplazar, formato condicional para detectar anomalías,
validación de datos para prevenirlas.

**SQL:** `DISTINCT`, `TRIM`, `LENGTH`, `SUBSTR`, `CAST`, `COALESCE`, `CASE WHEN` para estandarizar
categorías, `GROUP BY … HAVING COUNT(*) > 1` para hallar duplicados.

**Python (pandas):** `df.info()`, `df.describe()`, `df.isna().sum()`, `drop_duplicates()`,
`astype()`, `pd.to_datetime()`, `str.strip()` / `str.lower()`, `replace()`, `query()` para reglas
de negocio.

## 5. Documenta mientras limpias

Cada transformación registra: **qué**, **por qué**, **cómo**, **cuántas filas afectó** y **cuál fue
la alternativa descartada**. Ese último punto es el que distingue un caso de estudio de un tutorial.

Usa el formato de bitácora de `plantillas.md`. Escríbela en el momento, no después.

## 6. Verifica que la limpieza funcionó

- Reejecuta las pruebas de integridad de la fase 2 y compara antes/después.
- Reconciliación de conteos: filas iniciales − eliminadas = filas finales. Que cuadre exactamente.
- Revisa que las categorías estandarizadas sean el conjunto esperado, sin sorpresas.
- Verifica el resultado **contra el objetivo de negocio**, no solo contra reglas técnicas: si
  limpiar dejó el dataset sin la mitad del periodo relevante, la limpieza fue correcta y el análisis
  sigue siendo inviable.
- Si el proceso es un script, ejecútalo desde cero sobre el crudo. Si no reproduce el resultado, no
  está terminado.

---

## Puerta de salida

- [ ] Herramienta elegida y justificada.
- [ ] Cada tipo de dato sucio revisado explícitamente (aunque el resultado sea "no había").
- [ ] Bitácora completa con qué, por qué, cómo y cuántas filas por transformación.
- [ ] Reconciliación de conteos que cuadra.
- [ ] Valores atípicos investigados y la decisión sobre ellos justificada.
- [ ] Proceso reproducible desde el crudo.
- [ ] El dataset limpio sigue siendo suficiente para responder la pregunta.

## Errores comunes

- Eliminar nulos y atípicos por reflejo, sin mirar qué representan.
- Limpiar sobre el archivo original.
- Imputar valores sin declararlo, y luego reportar promedios como si fueran observados.
- Estandarizar categorías fusionando cosas que el negocio distingue.
- Documentar al final "más o menos lo que hice".
