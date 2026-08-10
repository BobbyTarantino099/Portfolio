# Fase 1 — Preguntar

**Objetivo:** convertir una situación difusa en una pregunta analítica que, al responderse, permita
tomar una decisión concreta.

**Entregable:** un enunciado claro de la tarea de negocio.

Esta es la fase que más casos de estudio arruina, porque es la más fácil de saltar. Un análisis
impecable sobre la pregunta equivocada no vale nada.

---

## 1. Separa el problema de negocio de la pregunta analítica

Son cosas distintas y hay que escribir las dos.

- **Problema de negocio:** lo que le duele a la organización. *"Los ingresos dependen de las
  membresías anuales y no estamos convirtiendo suficientes usuarios casuales."*
- **Pregunta analítica:** lo que los datos pueden responder. *"¿En qué difieren los patrones de uso
  entre miembros anuales y usuarios casuales?"*
- **Decisión que habilita:** qué se hará distinto según la respuesta. *"Definir el canal, el momento
  y el mensaje de la campaña de conversión."*

Si no puedes escribir la tercera línea, la pregunta no sirve todavía.

## 2. Identifica el tipo de problema

Clasificarlo orienta el método de análisis y el tipo de dato que necesitarás:

| Tipo | Qué busca | Ejemplo |
|---|---|---|
| Hacer predicciones | Estimar valores futuros | ¿Cuánta demanda habrá el próximo trimestre? |
| Categorizar cosas | Asignar a grupos según criterios | ¿Qué tipos de cliente existen? |
| Detectar algo inusual | Identificar lo fuera de lo normal | ¿Por qué cayó el tráfico esa semana? |
| Identificar temas | Agrupar categorías en conceptos mayores | ¿Qué motivos de queja se repiten? |
| Descubrir conexiones | Relacionar fenómenos que parecían independientes | ¿El clima afecta las ventas? |
| Encontrar patrones | Detectar comportamiento recurrente | ¿Hay estacionalidad semanal? |

## 3. Aplica pensamiento estructurado

- **Análisis de brecha:** describe el estado actual, describe el estado ideal, y el análisis vive
  en la distancia entre ambos.
- **Los cinco porqués:** pregunta "¿por qué?" cinco veces sobre el síntoma para llegar a la causa
  raíz. Evita analizar el síntoma en lugar del problema.
- **Las cinco W + H:** quién, qué, cuándo, dónde, por qué y cómo. Fuerza a explicitar el alcance.

## 4. Escribe preguntas SMART

Toda pregunta que guíe el análisis debe ser:

- **S**pecífica — apunta a un problema concreto, no a un tema general.
- **M**edible — se puede responder con datos cuantificables.
- **A**ccionable — la respuesta cambia lo que alguien hace.
- **R**elevante — importa para el problema, no solo es curiosa.
- **T**emporal — tiene un marco de tiempo definido.

**Además, deben ser justas.** Descarta:

- **Preguntas capciosas**, que empujan una respuesta: *"¿Qué tan satisfechos están los clientes con
  nuestro excelente servicio?"* → *"¿Qué tan satisfechos están los clientes con nuestro servicio?"*
- **Preguntas vagas**, sin criterio de respuesta: *"¿Va bien el producto?"*
- **Preguntas cerradas** cuando necesitas entender el porqué: *"¿Te gustó?"* → *"¿Qué cambiarías?"*
- **Preguntas compuestas**, que mezclan dos cosas y no se pueden responder de una vez.

## 5. Mapea a las partes interesadas

Para cada una registra: quién es, qué decisión toma, qué necesita ver, y qué formato prefiere.

- **Primarias:** aprueban o ejecutan la decisión. Su criterio define el éxito del análisis.
- **Secundarias:** proveen datos, contexto o validación técnica.

Acuerda explícitamente el **alcance del trabajo**: entregables, plazos, supuestos y — sobre todo —
qué queda *fuera*. La mayoría de los desastres de expectativas se originan aquí.

## 6. Define las métricas

Por cada pregunta, escribe la métrica que la responde con su **definición operativa**: fórmula
exacta, unidad, granularidad y ventana de tiempo. "Usuario activo" significa cosas distintas para
tres personas en la misma sala; la definición operativa cierra esa ambigüedad antes de que cueste
un rehacer.

---

## Puerta de salida

No avances a Preparar hasta que se cumpla todo esto:

- [ ] El problema de negocio está escrito en una o dos frases, sin jerga.
- [ ] La pregunta analítica es SMART y justa.
- [ ] Está escrita la decisión concreta que la respuesta habilitará.
- [ ] El tipo de problema está identificado.
- [ ] Las partes interesadas están mapeadas con lo que cada una necesita.
- [ ] Las métricas tienen definición operativa (fórmula, unidad, granularidad, ventana).
- [ ] El alcance incluye qué queda explícitamente fuera.

## Errores comunes

- Aceptar la pregunta tal como la formuló la parte interesada sin traducirla. Casi nunca es la
  pregunta correcta a la primera.
- Definir una métrica sin fórmula, y descubrirlo en la fase 4.
- Elegir el dataset primero y ajustar la pregunta después.
- Prometer responder tres preguntas cuando los datos solo alcanzan para una.

## Prompt de arranque

> Voy a iniciar un caso de estudio sobre [tema]. Ayúdame con la fase Preguntar: interrógame hasta
> tener el problema de negocio, la pregunta analítica SMART, la decisión que habilita, las partes
> interesadas y las métricas con definición operativa. No avances a la siguiente fase hasta que
> pasemos la puerta de salida.
