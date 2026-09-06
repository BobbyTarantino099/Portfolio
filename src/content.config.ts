import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

/**
 * El contrato de contenido, aplicado por codigo.
 *
 * Esto es la puerta de salida de la fase 7 del framework: si a un caso le falta
 * un campo obligatorio, `npm run build` FALLA. Un esquema que no puede romper la
 * construccion no esta haciendo su trabajo.
 *
 * Definicion completa en framework/caso-de-estudio-datos/references/portafolio.md,
 * seccion 2. La plantilla copiable es la numero 7 de plantillas.md.
 */

/** Taxonomia de tipos de problema de la fase 1. Un caso es exactamente uno de estos. */
const PROBLEM_TYPES = [
  'find patterns',
  'predict',
  'categorize',
  'spot something unusual',
  'identify themes',
  'discover connections',
] as const;

const cases = defineCollection({
  /**
   * Una carpeta por caso: cases/<slug>/index.md junto a cases/<slug>/images/.
   * Asi cada caso lleva sus propias figuras y el contrato puede referirlas como
   * ./images/... sin que dos casos compartan carpeta.
   * `generateId` quita el /index para que la URL sea /cases/<slug>/.
   */
  loader: glob({
    pattern: '**/index.md',
    base: './src/content/cases',
    generateId: ({ entry }) => entry.replace(/\/index\.md$/, ''),
  }),
  schema: ({ image }) =>
    z.object({
      /** EL HALLAZGO, no el tema. Es el titular de L1 y de L2 a la vez. */
      title: z.string().min(1),

      /** 2-3 frases. Es el parrafo de la tarjeta L1: no se escribe por separado. */
      summary: z.string().min(1),

      /** Visualizacion principal. Relativa al archivo del caso: ./images/... */
      hero: image(),

      /** Texto alternativo real. Obligatorio: sin esto la tarjeta es inaccesible. */
      heroAlt: z.string().min(1),

      date: z.coerce.date(),

      tools: z.array(z.string()).nonempty(),

      domain: z.string().min(1),

      problemType: z.enum(PROBLEM_TYPES),

      /** "125,855 games · 2 sources" — da la medida del caso de un vistazo. */
      scale: z.string().min(1),

      /**
       * Repositorio de evidencia (capa L3).
       * Opcional a proposito: un caso puede publicarse en el sitio antes de que su
       * repositorio sea publico. La puerta de salida del framework si lo exige para
       * dar el caso por terminado — pero eso lo revisa una persona, no el build.
       */
      repo: z.string().url().optional(),

      /** true -> aparece en la home. */
      featured: z.boolean().default(false),

      /**
       * Ruta publica al JSON de series de un explorador interactivo, si el caso trae uno.
       *
       * OPCIONAL a proposito, y esa es la parte que importa: los dos casos publicados antes de
       * que esto existiera no lo declaran, y tienen que seguir construyendo. Un campo nuevo
       * obligatorio habria roto el sitio entero para dar de alta una funcion que usa un caso.
       *
       * El JSON vive en `public/`, no en la carpeta del caso, porque el componente lo pide en
       * tiempo de ejecucion. Importarlo y embeberlo en el HTML meteria decenas de KB en cada
       * carga de la pagina aunque el lector no toque el explorador.
       *
       * Solo transporta AGREGADOS, como el resto del traspaso: si el archivo empieza a pesar
       * megas, la agregacion esta incompleta y se vuelve a la fase 4 del framework.
       */
      explorer: z.string().startsWith('/').optional(),

      /**
       * Reporte tecnico del caso: 9-11 paginas sobre COMO se hizo, servidas desde
       * `public/reports/`. Se copian desde el repositorio del caso con
       * `scripts/reports/sync_reports.py`, que ademas imprime el numero de paginas.
       *
       * OPCIONAL, por el mismo motivo que `explorer`: un caso puede publicarse antes
       * de tener su reporte, y un campo nuevo obligatorio habria roto el build de los
       * tres casos a la vez.
       *
       * `pages` viaja en el contrato en lugar de calcularse al construir: es lo que el
       * rail le promete al lector antes de que haga clic, y si alguien lo deja a medias
       * quiero que falle aqui y no en la pagina.
       */
      report: z
        .object({
          href: z.string().startsWith('/'),
          pages: z.number().int().positive(),
        })
        .optional(),

      /** Que demuestra este caso que los demas no. Alimenta la matriz de cobertura. */
      demonstrates: z.string().min(1),
    }),
});

const notes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/notes' }),
  schema: z.object({
    title: z.string().min(1),
    summary: z.string().min(1),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { cases, notes };
