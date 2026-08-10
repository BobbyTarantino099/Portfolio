// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // De aqui salen las URL absolutas: canonical y Open Graph. Tiene que apuntar
  // SIEMPRE a donde el sitio esta publicado de verdad. Un valor de relleno le dice
  // a Google que el contenido original vive en otro dominio, y puede dejar el sitio
  // sin indexar.
  // TODO(juanes): cambiar al dominio propio en cuanto este activo.
  site: 'https://portfolio.juanesa2002.workers.dev',

  // Salida estatica: no hay servidor. Cloudflare Pages sirve archivos.
  output: 'static',

  build: {
    // /cases/steam-price-reception/  en vez de  /cases/steam-price-reception.html
    format: 'directory',
  },
});
