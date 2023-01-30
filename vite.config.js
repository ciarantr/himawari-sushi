import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  root: resolve('./static/src'),
  base: '/static/src/',
  sever: {
    port: 3000,
    open: false,
  },
  build: {
    manifest: true,
    outDir: 'dist',
    assetsDir: '',
    rollupOptions: {
      input: {
        main: resolve('./static/src/js/main.ts'),
        style: resolve('./static/src/css/main.css')
      },
    }
  },
})
