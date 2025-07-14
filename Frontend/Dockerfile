FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

COPY tsconfig.json ./

RUN npm install

RUN npm install axios

RUN npm install -g typescript

COPY . .

EXPOSE 3000

CMD [ "npm", "run", "dev" ]