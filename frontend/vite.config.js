import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  preview: {
    host: "0.0.0.0",
    allowedHosts: [
      "harmonious-comfort-production-ac14.up.railway.app"
    ]
  },
  server: {
    host: "0.0.0.0",
    allowedHosts: [
      "harmonious-comfort-production-ac14.up.railway.app"
    ]
  }
});
