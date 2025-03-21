# Flask Secure API

A simple, secure Flask API to test DevSecOps pipelines and deployments.

## Endpoints

| Route      | Method | Description       |
|------------|--------|-------------------|
| `/hello`   | GET    | Returns a greeting|
| `/health`  | GET    | Health check      |

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
python app/main.py
```

## Docker

```bash
docker build -t flask-api-arm .
docker run -p 5000:5000 flask-api-arm
```

## Visit

- http://localhost:5000/hello
