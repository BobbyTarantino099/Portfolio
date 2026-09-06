/**
 * Datos del sitio, en un solo sitio.
 *
 * Los enlaces que no existan se dejan vacíos, no inventados: cada consumidor los
 * pinta condicionalmente, así que un campo vacío desaparece de la interfaz en vez
 * de publicar un enlace roto.
 */
export const site = {
  /** Nombre completo, como quieres que te lean los reclutadores. */
  name: 'Juan Esteban Arenas',

  /**
   * La letra del monograma. Una sola, a propósito: la caja es sólida y lo que se
   * reconoce de lejos es la forma, no las iniciales completas. `JEA` a 0.82rem
   * dentro del cuadro no se leía a tamaño de favicon, que es donde una marca
   * tiene que funcionar. Las figuras firman `JA` — ver estilo.py del framework.
   */
  initials: 'J',

  /** El rol, en una línea. Acompaña al nombre en cabecera y pie. */
  role: 'Data analyst',

  /** Una frase. Qué haces, no qué quieres ser. */
  tagline: 'Turning business questions into defensible recommendations.',

  /** Aparece en el <meta name="description"> de la home. */
  description:
    'Data analysis case studies: business question, real data, documented cleaning, and recommendations that state their own limits.',

  email: 'juanesa2002@gmail.com',

  links: {
    github: 'https://github.com/BobbyTarantino099',
    linkedin: 'https://www.linkedin.com/in/juan-a-702389312',
    /** Se genera con `python scripts/cv/build_cv.py`. */
    cv: '/cv.pdf',
    /* Aquí vivía `source`, el repositorio de este sitio, que enlazaba el colofón.
       El colofón ya no lo ofrece, así que el campo se va con él: un enlace que
       nadie pinta es una promesa que nadie comprueba. El repositorio sigue
       existiendo y siendo público. */
  },
} as const;

export const nav = [
  { href: '/', label: 'Work' },
  { href: '/method/', label: 'Method' },
  { href: '/notes/', label: 'Notes' },
  { href: '/about/', label: 'About' },
] as const;
