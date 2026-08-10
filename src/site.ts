/**
 * Datos del sitio, en un solo sitio.
 *
 * TODO(juanes): rellenar los marcadores. Estan deliberadamente vacios en vez de
 * inventados — un portafolio con datos de relleno publicados es peor que uno sin
 * publicar. Nada aqui deberia quedar como "TODO" el dia que el sitio salga.
 */
export const site = {
  /** Nombre como quieres que te lean los reclutadores. */
  name: 'Juanes',

  /** Una linea. Que haces, no que quieres ser. */
  tagline: 'Data analyst — turning business questions into defensible recommendations.',

  /** Aparece en el <meta name="description"> de la home. */
  description:
    'Data analysis case studies: business question, real data, documented cleaning, and recommendations that state their own limits.',

  email: 'juanesa2002@gmail.com',

  links: {
    github: '', // TODO: https://github.com/<usuario>
    linkedin: '', // TODO: https://www.linkedin.com/in/<usuario>
    cv: '', // TODO: /cv.pdf  (colocar el archivo en public/)
  },
} as const;

export const nav = [
  { href: '/', label: 'Work' },
  { href: '/method/', label: 'Method' },
  { href: '/notes/', label: 'Notes' },
  { href: '/about/', label: 'About' },
] as const;
