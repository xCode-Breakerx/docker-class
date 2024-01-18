FROM node:latest
LABEL authors="Code Breaker"
WORKDIR /app
COPY package*.json .
COPY server.js .
RUN npm install
# server port
EXPOSE 3000
ENTRYPOINT ["node", "server.js"]
#CMD ["node", "server.js"] # same thing