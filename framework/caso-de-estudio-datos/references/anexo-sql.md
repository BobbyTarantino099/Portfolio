# Anexo — SQL

Referencia operativa para las fases **Procesar** y **Analizar** cuando la herramienta elegida es SQL.
No es un curso de SQL: es el conjunto de prácticas que hacen que una consulta sea legible, correcta y
defendible en un caso de estudio.

---

## 1. Estilo: por qué importa en un portafolio

La consulta que publicas es un artefacto de comunicación. Alguien la va a leer para juzgar tu
criterio. Estas convenciones son las del certificado y las más extendidas en la industria:

| Elemento | Convención | Ejemplo |
|---|---|---|
| Cláusulas y funciones | MAYÚSCULAS | `SELECT`, `FROM`, `SUM()` |
| Nombres de columna | `snake_case`, minúsculas | `total_tickets` |
| Nombres de tabla | `CamelCase` o `snake_case`, consistente | `FavoriteMovies` |
| Longitud de línea | ≤ 100 caracteres | — |
| Comentario de una línea | `--` (no `#`: MySQL no lo reconoce) | `-- clave de unión` |
| Comentario de varias líneas | `/* ... */` | — |

**Nunca uses espacios en un alias.** `AS total tickets` hace que SQL lea solo `total`; el resto se
pierde en silencio.

**Siempre nombra las columnas calculadas.** Sin `AS`, obtienes `f0_`, `f1_`, `f2_` y el resultado es
ilegible tres semanas después.

```sql
/* Fecha:   2026-07-27
   Analista: Juanes
   Objetivo: viajes por tipo de usuario y día de la semana
*/
SELECT
  member_casual,
  day_of_week,
  COUNT(*)              AS total_viajes,   -- una fila = un viaje
  AVG(ride_length_min)  AS duracion_media
FROM
  CyclisticTrips
WHERE
  started_at BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY
  member_casual, day_of_week
ORDER BY
  member_casual, day_of_week;
```

### Comillas

Regla general: **comillas simples para cadenas**, en todos los dialectos. La excepción es cuando la
cadena contiene un apóstrofo:

```sql
WHERE favorite_food = 'Shepherd's pie'   -- ✗ error: la cadena termina en Shepherd
WHERE favorite_food = "Shepherd's pie"   -- ✓
```

### Sensibilidad a mayúsculas

No es uniforme entre dialectos y es una fuente clásica de resultados incompletos:

- **Sensibles:** BigQuery, Vertica. `country_code = 'us'` **no** devuelve las filas con `'US'`.
- **No sensibles:** MySQL, PostgreSQL, SQL Server (según collation).

Si no controlas el dialecto, normaliza explícitamente: `WHERE LOWER(country_code) = 'us'`. Y déjalo
anotado en la bitácora — es exactamente el tipo de decisión que la fase 3 pide documentar.

---

## 2. Estructura de una consulta compleja

El orden de escritura es fijo; el orden de ejecución no. Conocer ambos evita el 90 % de los errores
de `WHERE` vs `HAVING`.

```sql
SELECT      -- columnas que quieres ver
FROM        -- tabla de origen
WHERE       -- filtro sobre FILAS (antes de agregar)
GROUP BY    -- columna por la que agregas
HAVING      -- filtro sobre AGREGACIONES (después de agregar)
ORDER BY    -- orden del resultado, ASC o DESC
LIMIT       -- número máximo de filas
```

**Orden real de ejecución:** `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`.

Por eso no puedes usar un alias definido en `SELECT` dentro de un `WHERE`: cuando `WHERE` corre, el
alias todavía no existe.

**Atajo útil:** `GROUP BY 1, 2` se refiere a la posición de la columna en el `SELECT`. Ahorra tiempo,
pero se rompe silenciosamente si reordenas el `SELECT`. En una consulta que va al portafolio, escribe
los nombres.

---

## 3. JOINs: elegir bien o perder filas en silencio

| Tipo | Devuelve | Cuándo |
|---|---|---|
| `INNER JOIN` | Solo filas con coincidencia en **ambas** tablas | Por defecto. Es lo que casi siempre quiere el negocio, y es más rápido |
| `LEFT JOIN` | Todas las de la izquierda + coincidencias; `NULL` si no hay | Cuando el dato de la derecha es opcional ("nice to have") |
| `RIGHT JOIN` | Espejo del anterior | Raro; suele ser un `LEFT` mal escrito |
| `FULL OUTER JOIN` | Todo de ambas | Reconciliaciones, auditoría de cobertura |

**Protocolo obligatorio antes de aceptar un JOIN.** Es la causa nº 1 de resultados falsos y
espectaculares:

1. Cuenta las filas de la tabla izquierda **antes** de unir.
2. Cuenta las filas del resultado.
3. Si el resultado tiene **más** filas que la izquierda, la clave de unión no es única en la derecha
   → estás duplicando registros y todas tus sumas están infladas.
4. Si tiene **menos** con un `INNER JOIN`, estás perdiendo filas → verifica cuántas y por qué antes
   de continuar.
5. Anota los tres números en la bitácora.

```sql
-- Diagnóstico de duplicación en la clave de unión
SELECT
  friend,
  COUNT(*) AS n
FROM
  FavoriteMovies
GROUP BY
  friend
HAVING
  COUNT(*) > 1;
```

---

## 4. Agregación

`SUM()`, `COUNT()`, `AVG()`, `MAX()`, `MIN()` colapsan filas en un valor.

```sql
SELECT
  occasion,
  SUM(tickets)             AS total_tickets,
  COUNT(tickets)           AS n_compras,
  COUNT(DISTINCT tickets)  AS n_valores_distintos
FROM
  Purchases
GROUP BY
  occasion
HAVING
  SUM(tickets) > 5;
```

Notas de criterio:

- `DISTINCT` dentro de `COUNT()` es útil (usuarios únicos, sesiones únicas). Dentro de `SUM()` casi
  nunca tiene sentido.
- `COUNT(columna)` **ignora los nulos**; `COUNT(*)` los cuenta. Es la diferencia entre "cuántos
  registros hay" y "cuántos tienen dato". Elige a conciencia y dilo en el informe.
- `AVG()` también ignora nulos. Un promedio sobre una columna con 40 % de nulos no es el promedio de
  la población, es el promedio de quienes respondieron. Eso es sesgo de supervivencia disfrazado.
- `HAVING` es más caro que `WHERE` porque filtra después de agregar. Usa `WHERE` siempre que puedas.

---

## 5. Expresiones condicionales

### CASE — el caballo de batalla para estandarizar categorías

```sql
SELECT
  CASE
    WHEN genre = 'horror'      THEN 'No la veo'
    WHEN genre = 'documentary' THEN 'La veo solo'
    ELSE                            'La veo acompañado'
  END              AS categoria,
  COUNT(movie_title) AS n_peliculas
FROM
  MovieTheater
GROUP BY
  1;
```

Siempre incluye el `ELSE`. Sin él, todo lo que no encaje se vuelve `NULL` y desaparece de los
conteos sin avisar. Si quieres detectar lo no previsto, usa `ELSE 'SIN_CLASIFICAR'` y luego verifica
que esa categoría esté vacía.

### COALESCE — el primer valor no nulo

```sql
SELECT
  COALESCE(title_alternate, title_original, 'Sin título') AS titulo
FROM
  MovieLaunches;
```

Útil para consolidar campos redundantes. **Ojo:** rellenar nulos con `COALESCE(valor, 0)` en una
columna numérica convierte "no sé" en "cero" y arrastra el error hasta los promedios. Si lo haces,
declara la imputación en la bitácora.

---

## 6. Funciones de limpieza (fase 3)

| Necesidad | Función | Ejemplo |
|---|---|---|
| Quitar espacios sobrantes | `TRIM`, `LTRIM`, `RTRIM` | `TRIM(city)` |
| Unificar mayúsculas | `LOWER`, `UPPER` | `LOWER(country_code)` |
| Detectar longitudes anómalas | `LENGTH` | `WHERE LENGTH(zip) <> 5` |
| Extraer parte de un texto | `SUBSTR` | `SUBSTR(code, 1, 3)` |
| Cambiar de tipo | `CAST` | `CAST(price AS FLOAT64)` |
| Cambiar unidad | `CONVERT` (según dialecto) | — |
| Valores únicos | `DISTINCT` | `SELECT DISTINCT status` |
| Encontrar duplicados | `GROUP BY … HAVING COUNT(*) > 1` | ver arriba |
| Reemplazar texto | `REPLACE` | `REPLACE(phone, '-', '')` |

**Rutina de exploración de una columna categórica** — ejecútala siempre antes de limpiar:

```sql
SELECT
  status,
  COUNT(*) AS n
FROM
  Orders
GROUP BY
  status
ORDER BY
  n DESC;
```

Ahí aparecen los `Activo` / `activo` / ` Activo`, los tipeos y las categorías que nadie sabía que
existían.

---

## 7. Subconsultas, CTEs y tablas temporales

**Subconsulta (inner query):** anidada dentro de otra. Rápida de escribir, difícil de leer si se
anida más de un nivel.

**CTE con `WITH`:** la opción por defecto para cualquier consulta con más de dos pasos. Cada bloque
tiene nombre, se lee de arriba abajo y se puede reutilizar.

```sql
WITH viajes_limpios AS (
  SELECT
    ride_id,
    member_casual,
    TIMESTAMP_DIFF(ended_at, started_at, MINUTE) AS duracion_min
  FROM
    RawTrips
  WHERE
    ended_at > started_at        -- descarta duraciones imposibles
),

resumen AS (
  SELECT
    member_casual,
    COUNT(*)           AS n_viajes,
    AVG(duracion_min)  AS media_min
  FROM
    viajes_limpios
  GROUP BY
    member_casual
)

SELECT * FROM resumen ORDER BY n_viajes DESC;
```

**Tabla temporal:** existe solo durante la sesión. Útil cuando el mismo resultado intermedio se
consulta muchas veces y recalcularlo es caro.

```sql
CREATE TEMP TABLE ViajesLimpios AS
SELECT ...;

DROP TABLE ViajesLimpios;   -- limpieza explícita
```

Para un caso de portafolio, **prefiere CTEs**: se leen sin ejecutar nada y no dejan estado oculto.

---

## 8. Rutina de exploración de un dataset nuevo

Ejecuta esto antes de cualquier análisis. Es el equivalente SQL de `df.info()`:

```sql
-- 1. Volumen
SELECT COUNT(*) AS n_filas FROM Tabla;

-- 2. Rango temporal real
SELECT MIN(fecha) AS desde, MAX(fecha) AS hasta FROM Tabla;

-- 3. Nulos por columna crítica
SELECT
  COUNTIF(columna_a IS NULL) AS nulos_a,
  COUNTIF(columna_b IS NULL) AS nulos_b
FROM Tabla;

-- 4. Unicidad de la clave
SELECT COUNT(*) AS filas, COUNT(DISTINCT id) AS ids_unicos FROM Tabla;

-- 5. Extremos de cada campo numérico (los valores imposibles saltan aquí)
SELECT MIN(valor) AS minimo, MAX(valor) AS maximo, AVG(valor) AS media FROM Tabla;

-- 6. Cardinalidad de cada categórica
SELECT categoria, COUNT(*) AS n FROM Tabla GROUP BY categoria ORDER BY n DESC;
```

Los resultados de esta rutina van directo a la ficha de fuente (fase 2) y a la prueba de integridad
inicial.

---

## Puerta de salida específica de SQL

- [ ] Toda consulta publicada tiene cabecera con fecha, autor y objetivo.
- [ ] Todas las columnas calculadas tienen alias en `snake_case`.
- [ ] Cada JOIN tiene registrado el conteo antes/después y la explicación de la diferencia.
- [ ] Cada `CASE` tiene `ELSE`.
- [ ] Las imputaciones con `COALESCE` están declaradas en la bitácora.
- [ ] Se verificó el comportamiento de mayúsculas del dialecto usado.
- [ ] Consultas de más de dos pasos están escritas como CTEs, no como subconsultas anidadas.
- [ ] La consulta corre desde cero sobre los datos crudos y reproduce el resultado.

## Errores comunes

- Confundir `WHERE` con `HAVING` y filtrar antes de agregar cuando querías después (o al revés).
- Aceptar el resultado de un `JOIN` sin contar filas: la duplicación silenciosa infla todas las sumas.
- Usar `COUNT(*)` cuando querías `COUNT(columna)` y reportar como "clientes con dato" lo que en
  realidad son "registros".
- `SELECT *` en un caso de estudio: mueve columnas que no necesitas y oculta qué estás usando.
- Escribir `GROUP BY 1, 2` en la consulta final del repositorio y luego reordenar el `SELECT`.
- Olvidar que en BigQuery `'us'` ≠ `'US'`.
