# Anexo — Python y pandas

Referencia operativa para las fases **Procesar** y **Analizar** cuando la herramienta es Python.
Es la opción por defecto cuando el proceso debe ser reproducible, hay varios archivos que combinar,
o el volumen supera lo que una hoja de cálculo maneja con dignidad.

---

## 1. Estructura del notebook: el notebook *es* el caso de estudio

Un notebook publicado sin narrativa no es un caso de estudio, es un log de comandos. La estructura
que hace que se lea solo:

```
1. Título + una frase con la conclusión principal
2. Contexto: problema de negocio y pregunta analítica  [fase 1]
3. Fuentes y limitaciones                              [fase 2]
4. Carga y exploración inicial                         [fase 2]
5. Limpieza, con una celda markdown por decisión       [fase 3]
6. Análisis, con interpretación bajo cada resultado    [fase 4]
7. Visualizaciones con titular                         [fase 5]
8. Hallazgos, recomendaciones, limitaciones            [fase 6]
```

Reglas duras:

- **Cada bloque de código va precedido de una celda markdown que dice qué hace y por qué.** No qué
  hace la función — qué decisión analítica representa.
- **Cada resultado va seguido de una frase de interpretación.** Un `groupby` sin lectura es un
  número huérfano.
- **Reinicia el kernel y ejecuta todo de arriba abajo antes de publicar.** Si no corre limpio desde
  cero, el caso no es reproducible y esa es una de las ocho dimensiones de la rúbrica.
- **Sin rutas absolutas, sin credenciales.** `datos/crudos/archivo.csv`, no `C:\Users\...`.

---

## 2. Estructuras de datos: cuál usar

| Estructura | Mutable | Cuándo usarla |
|---|---|---|
| **Lista** `[]` | Sí | Colección ordenada que va a cambiar |
| **Tupla** `()` | No | Registro fijo; coordenadas; devolver varios valores de una función |
| **Diccionario** `{clave: valor}` | Sí | Búsqueda por clave; mapas de recodificación de categorías |
| **Conjunto** `set()` | Sí | Elementos únicos; operaciones de pertenencia e intersección |
| **Array NumPy** | Sí | Cálculo numérico vectorizado sobre datos homogéneos |
| **DataFrame pandas** | Sí | Datos tabulares. El caballo de batalla |

Dos usos que aparecen constantemente en un caso de estudio:

```python
# Diccionario para estandarizar categorías (fase 3)
mapa = {'bogota': 'Bogotá', 'BOGOTA D.C.': 'Bogotá', 'Bogotá D.C.': 'Bogotá'}
df['ciudad'] = df['ciudad'].replace(mapa)

# Conjunto para comparar cobertura entre dos fuentes (fase 2)
solo_en_a = set(df_a['id']) - set(df_b['id'])
print(f'{len(solo_en_a)} ids están en A pero no en B')
```

---

## 3. Fase 2 — Carga y exploración

```python
import pandas as pd
import numpy as np

df = pd.read_csv('datos/crudos/viajes_2025.csv')

df.shape          # (filas, columnas) — ¿coincide con lo que declara la fuente?
df.info()         # tipos y no-nulos por columna
df.head()         # inspección visual
df.describe()     # estadística descriptiva de las numéricas
df.describe(include='object')   # cardinalidad de las categóricas

df.isna().sum()                      # nulos por columna
df.isna().mean().sort_values(ascending=False)   # proporción de nulos

df['id'].nunique(), len(df)          # ¿la clave es única?
df['categoria'].value_counts(dropna=False)      # categorías reales, nulos incluidos
df['fecha'].min(), df['fecha'].max()            # rango temporal real vs esperado
```

Esta rutina alimenta directamente la ficha de fuente y la prueba de integridad inicial de la fase 2.
Cópiala tal cual; el orden importa menos que la exhaustividad.

**`describe()` es la primera línea de defensa contra valores imposibles.** Una duración mínima
negativa o una edad máxima de 300 aparecen aquí, no en la fase 4.

---

## 4. Fase 3 — Limpieza

```python
df_limpio = df.copy()          # nunca se modifica el crudo
n_inicial = len(df_limpio)

# --- Tipos ---
df_limpio['fecha']  = pd.to_datetime(df_limpio['fecha'], errors='coerce')
df_limpio['precio'] = pd.to_numeric(df_limpio['precio'], errors='coerce')
# errors='coerce' convierte lo no parseable en NaT/NaN.
# Cuenta cuántos generó: son datos que estabas perdiendo en silencio.
print('fechas no parseables:', df_limpio['fecha'].isna().sum() - df['fecha'].isna().sum())

# --- Texto ---
df_limpio['ciudad'] = (df_limpio['ciudad']
                       .str.strip()
                       .str.lower()
                       .str.replace(r'\s+', ' ', regex=True))

# --- Duplicados ---
n_dup = df_limpio.duplicated(subset=['id']).sum()
df_limpio = df_limpio.drop_duplicates(subset=['id'])
print(f'duplicados eliminados: {n_dup}')

# --- Reglas de negocio ---
n_imposibles = (df_limpio['duracion_min'] <= 0).sum()
df_limpio = df_limpio.query('duracion_min > 0')
print(f'duraciones imposibles eliminadas: {n_imposibles}')

# --- Columnas derivadas ---
df_limpio['dia_semana'] = df_limpio['fecha'].dt.day_name()
df_limpio['mes']        = df_limpio['fecha'].dt.to_period('M')

# --- Reconciliación ---
print(f'{n_inicial} - {n_dup} - {n_imposibles} = {len(df_limpio)}')
assert n_inicial - n_dup - n_imposibles == len(df_limpio)
```

**El `assert` final no es decorativo.** Es la reconciliación de conteos de la fase 3 convertida en
código: si el proceso deja de cuadrar, el notebook falla en vez de producir un resultado silenciosa-
mente equivocado.

Cada `print` de esta celda va también a la bitácora de limpieza, con el "por qué" y la alternativa
descartada.

**Sobre los nulos:** `dropna()` sin argumentos elimina toda fila con cualquier nulo. Es casi siempre
demasiado agresivo. Especifica: `dropna(subset=['columna_crítica'])`. Y si imputas, déjalo explícito
y no vuelvas a llamar "promedio observado" al resultado.

---

## 5. Fase 4 — Análisis

```python
# Filtrado booleano (boolean masking)
casuales = df_limpio[df_limpio['tipo_usuario'] == 'casual']
finde    = df_limpio[df_limpio['dia_semana'].isin(['Saturday', 'Sunday'])]

# Agrupación y agregación — el corazón del análisis
resumen = (df_limpio
           .groupby('tipo_usuario')
           .agg(n_viajes   = ('id', 'count'),
                media_min  = ('duracion_min', 'mean'),
                mediana_min= ('duracion_min', 'median'),
                p90_min    = ('duracion_min', lambda s: s.quantile(0.90)))
           .round(2))

# Dos dimensiones
tabla = df_limpio.pivot_table(index='dia_semana',
                              columns='tipo_usuario',
                              values='duracion_min',
                              aggfunc='median')

# Unir fuentes — verifica siempre el tamaño antes y después
antes = len(df_limpio)
df_join = df_limpio.merge(df_estaciones, on='estacion_id', how='left')
print(f'antes: {antes} · después: {len(df_join)}')
assert len(df_join) == antes, 'el merge duplicó filas: la clave no es única en la derecha'

# Series de tiempo
serie = df_limpio.set_index('fecha')['duracion_min'].resample('W').median()

# Relación entre variables
df_limpio[['duracion_min', 'distancia_km', 'temperatura']].corr()
```

**El `assert` después del `merge` es obligatorio.** Un `merge` que duplica filas infla todas las
sumas posteriores y el error no da ninguna señal.

**Siempre media y mediana juntas.** Y cuando difieran, reporta la mediana y explica por qué.

**`corr()` mide asociación lineal, nada más.** Escribe "correlación no implica causalidad" en el
informe cada vez que muestres una. No es una formalidad: es la pregunta que te van a hacer.

---

## 6. Fase 5 — Visualización

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=resumen.reset_index(), x='tipo_usuario', y='mediana_min',
            palette=['#9e9e9e', '#1f77b4'], ax=ax)   # gris = contexto, color = protagonista

ax.set_title('Los usuarios casuales viajan 2.3× más tiempo que los miembros',
             fontsize=14, weight='bold', loc='left')
ax.set_xlabel('')
ax.set_ylabel('Duración mediana (minutos)')
ax.set_ylim(bottom=0)                 # en barras, el eje SIEMPRE empieza en cero
sns.despine()                          # relación tinta/dato

for c in ax.containers:
    ax.bar_label(c, fmt='%.1f')       # etiquetas directas, sin leyenda

fig.savefig('salidas/graficos/duracion_por_tipo.png', dpi=150, bbox_inches='tight')
```

Checklist por figura, alineado con la fase 5:

- [ ] El título enuncia el hallazgo, no el tema.
- [ ] El eje de una barra empieza en cero.
- [ ] Un color destaca; el resto es gris.
- [ ] Etiquetas directas donde quepan, en lugar de leyenda.
- [ ] Ordenado por valor, no alfabéticamente.
- [ ] Exportado con `bbox_inches='tight'` y `dpi` suficiente para el medio real.
- [ ] Texto alternativo escrito para el README.

El detalle de elección de tipo de gráfico, diseño y accesibilidad está en `anexo-visualizacion.md`.

---

## 7. Exportar los resultados

```python
df_limpio.to_csv('datos/limpios/viajes_limpios.csv', index=False)
resumen.to_csv('salidas/tablas/resumen_por_tipo.csv')
```

`index=False` salvo que el índice signifique algo. Si no, cada exportación añade una columna
`Unnamed: 0` que después alguien tiene que limpiar.

---

## Puerta de salida específica de Python

- [ ] El notebook corre completo desde kernel reiniciado, sin errores.
- [ ] Sin rutas absolutas, credenciales ni claves.
- [ ] Cada celda de código tiene una celda markdown antes que explica la decisión.
- [ ] Cada resultado tiene una frase de interpretación después.
- [ ] Reconciliación de conteos implementada como `assert`.
- [ ] Todo `merge` verificado con `assert` sobre el número de filas.
- [ ] Los datos crudos nunca se sobrescriben (`df.copy()` desde el inicio).
- [ ] `requirements.txt` o lista de versiones incluida.
- [ ] Las figuras están guardadas como archivos, no solo renderizadas en el notebook.

## Errores comunes

- Modificar `df` in situ y perder la trazabilidad de qué había antes.
- `dropna()` sin `subset`: elimina filas por nulos en columnas que no importaban.
- `merge` sin verificar el conteo: duplicación silenciosa que infla todas las agregaciones.
- `errors='coerce'` sin contar cuántos valores se volvieron `NaN`.
- Publicar el notebook con celdas ejecutadas en desorden (`In [17]`, `In [3]`, `In [42]`).
- Notebook con más código que narrativa: técnicamente correcto, inútil como caso de estudio.
- Dejar `SettingWithCopyWarning` sin resolver — casi siempre indica que estás escribiendo sobre una
  vista y el cambio puede no aplicarse.
