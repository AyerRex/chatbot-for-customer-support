import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // Make the Docker container accessible from the outside(corresponding host: '0.0.0.0')
    host: true, 
    port: 5173,
    // Optimization: for windows listening and rebuild
    watch: {
      usePolling: true
    }
  }
})