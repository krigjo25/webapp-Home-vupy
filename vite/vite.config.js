// Vite configurations are defined here.
// Read more about Vite configurations: https://vitejs.dev/config/

// Importing the vite plugins
import { defineConfig } from 'vite'
const { resolve } = require('path')

const { defineConfig } = require('vite')


export default defineConfig({
  esbuild: {
      jsxInject: `import React from 'react'`
  },
  server: {
    port: 3000,
    strictPort: true,
  },

  resolve: {
    alias: {
      '@': '/static/js',
    }
  },
});