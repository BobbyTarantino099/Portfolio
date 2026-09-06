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

  /** Iniciales del monograma de la cabecera. */
  initials: 'JEA',

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
    /** Repositorio de este sitio, para el colofón del pie. */
    source: 'https://github.com/BobbyTarantino099/Portfolio',
  },
} as const;

export const nav = [
  { href: '/', label: 'Work' },
  { href: '/method/', label: 'Method' },
  { href: '/notes/', label: 'Notes' },
  { href: '/about/', label: 'About' },
] as const;
