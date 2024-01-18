FROM gcc:latest
LABEL authors="Code Breaker"
COPY main.cpp .
RUN gcc main.cpp -lstdc++ -o main
ENTRYPOINT ["./main"]