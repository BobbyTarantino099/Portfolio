// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // Cambiar al dominio real cuando se compre. Se usa para URLs absolutas
  // (canonical, Open Graph, sitemap). No afecta al desarrollo local.
  site: 'https://example.com',

  // Salida estatica: no hay servidor. Cloudflare Pages sirve archivos.
  output: 'static',

  build: {
    // /cases/steam-price-reception/  en vez de  /cases/steam-price-reception.html
    format: 'directory',
  },
});
