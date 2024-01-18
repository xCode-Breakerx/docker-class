FROM postgres:latest
LABEL authors="Code Breaker"
ENV POSTGRES_PASSWORD db
ENV POSTGRES_DB db
ENV POSTGRES_USER db
# expose this port to allow coms (default postgres port)
EXPOSE 5432
COPY db.sql /docker-entrypoint-initdb.d/
