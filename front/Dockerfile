# Etapa 1: Construcción del frontend
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

# Etapa 2: Servidor NGINX para producción
FROM nginx:alpine

# Copiamos el build generado por React a la carpeta de nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Reemplazamos el default.conf para servir una SPA correctamente (React Router)
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]


