FROM python:3.12-slim

WORKDIR /crow

RUN pip install docker flask

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        vim \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# CMD ["python3", "-u", "crow.py"]

CMD ["python3", "-u", "crow.py"]

# CMD ["tail", "-f", "/dev/null"]