// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // De aqui salen las URL absolutas: canonical y Open Graph. Tiene que apuntar
  // SIEMPRE a donde el sitio esta publicado de verdad, y ser una URL completa:
  // sin el protocolo, Astro falla la construccion con "Invalid URL".
  site: 'https://juanesportfolio.com',

  // Salida estatica: no hay servidor. Cloudflare Workers sirve los archivos.
  output: 'static',

  build: {
    // /cases/steam-price-reception/  en vez de  /cases/steam-price-reception.html
    format: 'directory',
  },
});
