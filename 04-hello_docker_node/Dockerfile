FROM node:latest
LABEL authors="Code Breaker"
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 7969
ENTRYPOINT ["node", "server.js"]
#CMD ["node", "server.js"] # same thing