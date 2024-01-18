FROM node:latest
LABEL authors="Code Breaker"
WORKDIR /app/back
COPY package.json .
COPY server.js .
RUN npm install
EXPOSE 3021
CMD ["node", "server.js"]



