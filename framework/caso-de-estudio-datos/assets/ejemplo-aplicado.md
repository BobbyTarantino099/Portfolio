# Ejemplo aplicado

El framework recorrido de punta a punta sobre un caso de bicicletas compartidas, para mostrar la
*forma* que debe tener cada entregable. Las cifras son ilustrativas.

---

## Fase 1 — Preguntar

- **Problema de negocio:** las membresías anuales son sustancialmente más rentables que los pases
  sueltos, y el crecimiento depende de convertir usuarios casuales en miembros.
- **Pregunta analítica:** ¿en qué difieren los patrones de uso entre miembros anuales y usuarios
  casuales durante los últimos 12 meses?
- **Decisión que habilita:** definir el momento, el lugar y el mensaje de la campaña de conversión.
- **Tipo de problema:** encontrar patrones + descubrir conexiones.
- **Partes interesadas:** dirección de marketing (aprueba la campaña, necesita ver diferencias
  accionables); equipo ejecutivo (aprueba el presupuesto, necesita magnitud y confianza).
- **Métricas:** duración media y mediana del viaje por tipo de usuario; viajes por día de la semana;
  distribución horaria; estacionalidad mensual. Granularidad: un viaje. Ventana: 12 meses.
- **Fuera de alcance:** por restricciones de privacidad no se cruzan viajes con datos de compra, así
  que no se puede saber si un usuario casual repite ni dónde reside.

**Nota de criterio:** la limitación de privacidad se detecta en la fase 1, no en la 4. Eso ahorra
una semana de trabajo perdido.

## Fase 2 — Preparar

- **Fuente:** registros históricos de viajes publicados por el operador, primera parte, licencia
  pública, 12 archivos mensuales, ~5.7 M filas. Una fila = un viaje.
- **ROCCC:** R sí (sistema de registro automático), O sí (fuente primaria), C parcial —no hay
  demografía—, C sí (últimos 12 meses), C sí.
- **Sesgos:** los viajes con estación de origen o destino nula pueden concentrarse en zonas con
  fallo de geolocalización; se revisa si su distribución geográfica es aleatoria antes de excluirlos.
- **Integridad inicial:** 5.719.877 filas; rango de fechas completo; 0.9 % de nulos en estación de
  destino; duraciones entre −12 s y 38 días (ambos extremos imposibles).

## Fase 3 — Procesar

Herramienta: Python con pandas, porque hay que aplicar el mismo proceso a 12 archivos y debe ser
reproducible. Una hoja de cálculo no soporta el volumen.

| # | Transformación | Por qué | Filas | Alternativa descartada |
|---|---|---|---|---|
| T1 | Unificar esquema de los 12 archivos | Dos meses renombraron columnas | — | Procesar por separado: impide el análisis anual |
| T2 | Derivar `duracion_min` y `dia_semana` | La pregunta lo exige | — | — |
| T3 | Excluir duraciones ≤ 60 s | Falsos arranques, no viajes reales | 87.432 (1.5 %) | Conservarlos: distorsiona la mediana a la baja |
| T4 | Excluir duraciones > 24 h | Bicicletas no devueltas, no uso | 3.104 (0.05 %) | Winsorizar: oculta un problema operativo real |
| T5 | Estandarizar `tipo_usuario` | Tres etiquetas para dos categorías | — | — |

Reconciliación: 5.719.877 − 90.536 = 5.629.341. ✅

## Fase 4 — Analizar

- **H1:** la duración mediana del usuario casual es de 21.4 min frente a 9.8 min del miembro
  (2.2×). Verificado con recálculo por consulta independiente. La media difiere más que la mediana
  por asimetría, así que se reporta la mediana.
- **H2:** los viajes de miembros se concentran de lunes a viernes con picos a las 8 y las 17 h;
  los casuales se concentran en sábado y domingo, entre las 11 y las 16 h.
- **H3:** el volumen casual cae 71 % en invierno frente al pico de verano; el de miembros, 34 %.
- **Lectura alternativa descartada:** que la diferencia de duración se debiera a tipos de bicicleta
  distintos. Se desagregó por tipo y el patrón se mantiene en todos.
- **No respondido:** cuántos usuarios casuales son turistas. Requeriría datos que no existen aquí.

## Fase 5 — Compartir

Gráfico 1 — barras horizontales. Titular: *"El usuario casual pedalea el doble de tiempo que el
miembro"*. Color destacado en casual, gris en miembro, eje desde cero, valores etiquetados.

Gráfico 2 — líneas por día de la semana, dos series. Titular: *"Los miembros usan la bici para ir al
trabajo; los casuales, para pasear el fin de semana"*. Anotación sobre el cruce del sábado.

Q&A preparado, pregunta más dura: *"¿Cómo sabes que no son los mismos usuarios en distintos
momentos?"* Respuesta: no se puede saber con estos datos, es una limitación declarada; las
recomendaciones están diseñadas para funcionar bajo ambos supuestos.

## Fase 6 — Actuar

**R1 — Lanzar una membresía de fin de semana.**
Evidencia: H2, el 68 % de los viajes casuales ocurre sábado y domingo. Impacto esperado: conversión
del 3-5 % de los casuales recurrentes, asumiendo elasticidad similar a la del plan anual. Métrica:
altas de fin de semana a 90 días. Riesgo: puede canibalizar altas del plan anual — se mide con la
proporción entre ambos. Esfuerzo: medio.

**R2 — Concentrar la pauta digital de mayo a agosto**, cuando el volumen casual está en su pico
(H3). Métrica: costo por adquisición comparado contra la campaña continua del año anterior.
Esfuerzo: bajo.

**R3 — Ubicar la promoción física en las estaciones con mayor proporción de viajes casuales de fin
de semana.** Métrica: canjes por estación. Riesgo: la señal de estación tiene 0.9 % de nulos, se
excluyen del ranking. Esfuerzo: bajo.

**Limitaciones:** sin datos demográficos ni de residencia; sin identificador de usuario, no se
distingue un casual recurrente de uno único; ventana de 12 meses, insuficiente para separar
tendencia de estacionalidad plurianual.
