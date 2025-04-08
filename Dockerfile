# Dockerfile vulnérable

FROM ubuntu:latest
USER root
RUN apt-get update && apt-get install -y curl

# Copie sans USER non root
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]
