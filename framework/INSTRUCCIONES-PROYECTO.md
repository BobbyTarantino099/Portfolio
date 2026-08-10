# Cómo usar el framework en un Proyecto de Claude

Guía de instalación y uso de la skill `caso-de-estudio-datos` dentro de un Proyecto de Claude.

---

## Instalación (una sola vez)

### 1. Crea el proyecto

Claude → **Proyectos** → **Crear proyecto**. Nombre sugerido: *Casos de estudio de datos*.

### 2. Sube los archivos al conocimiento del proyecto

Arrastra los **19 archivos `.md`** de la carpeta `caso-de-estudio-datos`, incluidos los que están en
`references/` y `assets/`. El proyecto no conserva la estructura de carpetas, pero los nombres son
únicos y no hay conflicto.

> El archivo `.zip` **no sirve** para un Proyecto. Es para Claude Code, donde se descomprime en
> `.claude/skills/`.

**No subas al conocimiento del proyecto:** archivos de datos (CSV, XLSX), notebooks ni salidas. Esos
van en los chats individuales porque cambian de un caso a otro.

### Estructura de carpetas en tu computador

El conocimiento del proyecto (los 19 `.md`) es la copia que usa Claude en el chat. Localmente,
mantén **una sola copia** de `framework/caso-de-estudio-datos/` en la raíz, no dentro de cada caso:

```
portafolio/
├── framework/
│   └── caso-de-estudio-datos/     # una sola copia, la misma para todos los casos
├── site/                          # el sitio publicado  [repositorio propio]
└── cases/
    ├── steam-price-reception/     # [repositorio propio]
    │   ├── CASO.md
    │   ├── documentacion/
    │   ├── datos/{crudos,intermedios,limpios}/
    │   ├── notebooks/
    │   ├── salidas/{graficos,tablas}/
    │   └── entregables/
    └── siguiente-caso/
        └── ... (misma estructura)
```

Un repositorio por caso, más uno para el sitio. Si aparece una segunda copia del framework dentro
de la carpeta de un caso, bórrala: dos copias divergen en semanas y deja de estar claro cuál manda.

Cuando un caso cierra la fase 6, entrega al sitio **un** Markdown con front-matter más sus figuras
y tablas agregadas — nada más. El contrato está en `portafolio.md`, sección 2, y la plantilla es la
número 7 de `plantillas.md`.

### 3. Pega las instrucciones del proyecto

Copia el bloque completo en **Instrucciones del proyecto**:

```
Sigue el framework de SKILL.md para todo trabajo de análisis de datos.

Reglas:
1. Lee el archivo de referencia de la fase ANTES de ejecutarla. No trabajes de memoria.
2. En Procesar y Analizar, lee también el anexo de la herramienta elegida
   (anexo-sql.md, anexo-hojas-de-calculo.md o anexo-python.md).
   En Compartir, lee anexo-visualizacion.md.
3. No avances de fase sin pasar su puerta de salida punto por punto.
   Enuncia qué se cumplió y qué no.
4. Confírmame el entregable antes de pasar a la siguiente fase.
   Las decisiones de negocio y de alcance son mías, no tuyas.
5. Nada de datos inventados. Si un número no salió de los datos, no entra al informe.
6. Mantén actualizado CASO.md al cerrar cada fase.

Responde en español.
```

---

## Uso diario

### Un chat por fase

Cada fase en una conversación distinta dentro del mismo proyecto. Al empezar la siguiente, pega tu
`CASO.md` actualizado. Esto mantiene el contexto limpio y mejora bastante la calidad de las
respuestas.

### Prompts de arranque

**Fase 0 — no tengo tema todavía**

> Ayúdame con la fase 0. Quiero un caso sobre [sector]. Usa `eleccion-del-caso.md` e interrógame
> hasta rellenar la ficha de decisión. No avancemos hasta pasar la puerta de salida.

**Fase 1 — ya tengo tema y datos**

> Voy a iniciar un caso sobre [tema]. Empecemos por la fase 1 siguiendo `01-preguntar.md`.
> Interrógame hasta tener el problema de negocio, la pregunta analítica SMART, la decisión que
> habilita, las partes interesadas y las métricas con definición operativa.

**Practicar con un caso listo**

> Usa el brief de [Cyclistic / Bellabeat] de `briefs-capstone.md`. Empecemos por la fase 1.

**Fases 2 a 6 — continuar**

> Aquí está mi CASO.md actualizado. Cerramos la fase [N-1]. Sigamos con la fase [N] usando
> `0N-[nombre].md`. [Si aplica: la herramienta es Python, lee también anexo-python.md.]

**Revisión final**

> El caso está terminado. Aplícame `criterios-de-calidad.md`: puntúa las ocho dimensiones y
> respóndeme las siete preguntas de revisión final. Sé duro.

**Cerrar el portafolio**

> Usa `portafolio.md`. Ayúdame a rellenar la matriz de cobertura con mis casos actuales y a decidir
> qué debería demostrar el siguiente.

---

## Cuándo cada archivo

| Situación | Archivo |
|---|---|
| No sé qué caso hacer | `eleccion-del-caso.md` |
| Definir la pregunta | `01-preguntar.md` |
| Evaluar y documentar fuentes | `02-preparar.md` |
| Limpiar datos | `03-procesar.md` + anexo de la herramienta |
| Calcular y verificar | `04-analizar.md` + anexo de la herramienta |
| Gráficos y presentación | `05-compartir.md` + `anexo-visualizacion.md` |
| Recomendaciones y publicar | `06-actuar.md` |
| Estrategia del portafolio | `portafolio.md` |
| Necesito una plantilla | `plantillas.md` |
| Revisión antes de publicar | `criterios-de-calidad.md` |
| No sé qué significa un término | `glosario.md` |
| Quiero practicar sin decidir | `briefs-capstone.md` |

---

## Alternativa: Claude Code

Si prefieres trabajar desde la terminal:

1. Descomprime `caso-de-estudio-datos.zip` dentro de `.claude/skills/` en la carpeta del proyecto
   (o en `~/.claude/skills/` para tenerla siempre disponible).
2. La skill se activa sola cuando menciones un caso de estudio, un dataset o un análisis.
3. También puedes forzarla: `Usa la skill caso-de-estudio-datos. Empecemos la fase 1 sobre [tema].`

Ventaja sobre el Proyecto: Claude Code lee los archivos bajo demanda, así que la divulgación
progresiva funciona sola y puede además ejecutar el código del análisis.

---

## Errores que arruinan el resultado

- **Subir el zip** en vez de los archivos sueltos. El Proyecto no lo descomprime.
- **Dejar las instrucciones del proyecto vacías.** Sin ellas, Claude tratará los archivos como
  documentos de consulta, no como un framework que debe seguir.
- **Hacer las seis fases en un solo chat.** El contexto se satura y las últimas fases salen flojas.
- **Dejar que Claude decida el alcance.** Las decisiones de negocio son tuyas; si no las tomas tú,
  el caso no es tuyo.
- **Saltar las puertas de salida** porque "ya se entiende". Son lo que separa este framework de una
  conversación normal sobre datos.
