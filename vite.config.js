import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  root: resolve('./static/src'),
  base: '/static/',

  build: {
    manifest: true,
    outDir: resolve('./static/dist'),
    assetsDir: '',
    rollupOptions: {
      input: {
        main: resolve('./static/src/js/main.ts'),
        editBookingDialog: resolve('./static/src/js/editBookingDialog.ts'),
        bookingInputUpdate: resolve('./static/src/js/confirmationDialog.ts'),
      },
    },
  },
})
