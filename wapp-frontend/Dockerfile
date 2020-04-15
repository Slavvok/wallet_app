FROM node:12 as builder
ARG PRODUCTION_URL
#ENV PRODUCTION_URL $PRODUCTION_URL
ENV PATH /app/node_modules/.bin:$PATH
WORKDIR /app
COPY package.json /app/package.json
RUN npm install
RUN npm install -g @angular/cli
COPY . /app
RUN ng build --prod --build-optimizer --output-path=dist

FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY ./nginx.conf /etc/nginx/conf.d/
COPY --from=builder /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
