# Criterios de calidad

Revisión final antes de publicar. Léela con la actitud de quien intenta encontrarle fallas al caso,
no de quien quiere darlo por terminado.

---

## Rúbrica

Puntúa cada dimensión de 1 a 3. Un caso listo para portafolio no tiene ningún 1.

| Dimensión | 1 — insuficiente | 2 — aceptable | 3 — sólido |
|---|---|---|---|
| **Pregunta** | Tema general, sin decisión asociada | Pregunta clara pero sin métrica definida | SMART, con decisión y métrica operativa |
| **Datos** | Fuente sin documentar | Fuente citada | Ficha completa, ROCCC evaluado, sesgos declarados |
| **Limpieza** | Sin documentar | Se describe qué se hizo | Bitácora con qué, por qué, cuántas filas y alternativas |
| **Análisis** | Solo promedios y conteos | Comparaciones y tendencias | Verificado, cuantificado, con lecturas alternativas descartadas |
| **Visualización** | Gráficos por defecto | Correctos y legibles | Titular con hallazgo, accesibles, diseño intencional |
| **Recomendaciones** | Genéricas o ausentes | Concretas | Con evidencia, métrica, riesgo y esfuerzo |
| **Honestidad** | Sin limitaciones | Limitaciones mencionadas | Limitaciones, supuestos y datos faltantes explícitos |
| **Reproducibilidad** | No reproducible | Pasos descritos | Ejecutable desde el crudo por un tercero |

---

## Señales de un caso mediocre

Si reconoces alguna, hay trabajo pendiente:

- El titular del caso nombra un tema, no una conclusión.
- No se puede decir en una frase qué decisión cambia el análisis.
- La sección de limpieza dice "se limpiaron los datos" sin más.
- Todos los gráficos son del mismo tipo, o son los que la herramienta ofrece por defecto.
- Secciones enteras en prosa corrida donde había una enumeración: un párrafo que anuncia «tres
  decisiones» y luego las encadena con comas obliga a leerlo dos veces para extraer una lista que
  el autor ya tenía en la cabeza.
- Las recomendaciones servirían igual para otra empresa de otro sector.
- No hay ninguna limitación declarada.
- Hay más código que narrativa.
- Ningún número del informe se puede rastrear hasta un cálculo concreto.
- El análisis confirmó exactamente la hipótesis inicial, sin ninguna sorpresa. (Posible, pero
  merece una segunda revisión: suele indicar sesgo de confirmación.)

---

## Revisión final: siete preguntas

Respóndelas por escrito antes de publicar.

1. Si un directivo lee solo el titular y la primera visualización, ¿se lleva el mensaje correcto?
2. ¿Puede otra persona reproducir el resultado partiendo únicamente del repositorio?
3. ¿Cada cifra del informe se rastrea hasta un cálculo documentado?
4. ¿Cuál es la crítica más fuerte que alguien podría hacerle a este análisis, y está respondida?
5. ¿Hay algo que quisiera esconder? (Si lo hay, ese es exactamente el punto que hay que declarar.)
6. ¿Qué habilidad demuestra este caso que los otros del portafolio no?
7. ¿Puedo explicarlo entero en tres minutos, sin diapositivas?

---

## Antes de publicar

- [ ] Sin datos personales identificables en el repositorio ni en los gráficos.
- [ ] Licencias de todas las fuentes respetadas y citadas.
- [ ] Enlaces funcionando; imágenes visibles en el README sin descargar nada.
- [ ] Sin credenciales, rutas locales ni claves en notebooks o scripts.
- [ ] Ortografía y cifras revisadas — un error tipográfico en un número destruye la credibilidad de
      todos los demás.
- [ ] Párrafo de introducción escrito para el índice del portafolio.
- [ ] **Formato del texto revisado en la página publicada y en el `README`**: las enumeraciones son
      listas, los datos de dos dimensiones son tablas, y no queda ningún párrafo de más de ~70
      palabras que no sea deliberadamente argumental. La regla y sus señales están en la
      plantilla 7 de `plantillas.md`.
