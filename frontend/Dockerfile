FROM node:18-alpine as node

WORKDIR /app

COPY app/package* ./
RUN npm i

CMD [ "npm", "run", "dev" ]