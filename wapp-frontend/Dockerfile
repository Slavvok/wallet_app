FROM node:alpine as builder
ARG PRODUCTION_URL
ENV PRODUCTION_URL $PRODUCTION_URL
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install @angular/cli -g
RUN npm i && cp -R ./node_modules ./app
COPY . .
RUN npm run build --prod --build-optimizer --output-path=dist

FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY ./nginx.conf /etc/nginx/conf.d/
COPY --from=builder /app/dist/wapp-frontend /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
