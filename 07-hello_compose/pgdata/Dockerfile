FROM postgres:latest
LABEL authors="Code Breaker"
ENV POSTGRES_PASSWORD exo5
ENV POSTGRES_DB exo5
ENV POSTGRES_USER postgres
COPY db.sql /docker-entrypoint-initdb.d/
EXPOSE 5432