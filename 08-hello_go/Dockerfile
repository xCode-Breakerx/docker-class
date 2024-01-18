FROM golang:latest
LABEL authors="Code Breaker"
COPY main.go .
RUN go build main.go
EXPOSE 8000
ENTRYPOINT ["./main"]