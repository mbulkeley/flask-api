
# Flask + SOAP + MariaDB API (Raspberry Pi Project)

[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi-red)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A simple full-stack API project built with Flask and MariaDB — containerized using Docker Compose and deployable to a Raspberry Pi. Includes REST and SOAP endpoints and auto-seeded database. Two HTML dashboards included for REST and SOAP testing.

Using as I brush up on some skills with my Raspberry Pi.

---

## Features

- REST API built with Flask
- SOAP API using Spyne (accessible at `/soap`)
- Data stored in MariaDB
- Containerized with Docker Compose
- `.env` support for secure credentials
- Auto-creates & seeds a greetings table
- HTML dashboards for REST and SOAP
- Tested on Raspberry Pi (ARMv8)

---

## Setup

### 1. Clone the Repo

Clone using SSH:

```bash
git clone git@github.com:captchaos/flask-api.git
cd flask-api
```

Or with HTTPS:

```bash
git clone https://github.com/captchaos/flask-api.git
cd flask-api
```

---

### 2. Create a `.env` File

```env
MYSQL_ROOT_PASSWORD=yourpassword
MYSQL_DATABASE=flaskdb
MYSQL_USER=flaskuser
MYSQL_PASSWORD=yourpassword
DB_HOST=db
```

> **Don't commit your `.env` file** — it's in `.gitignore`.

---

### 3. Build and Run

```bash
docker compose up --build
```

---

## Accessing the App

### REST Dashboard:

```
http://<pi-ip>:5000/
```

### SOAP Dashboard:

```
http://<pi-ip>:5000/soap-ui
```

> Replace `<pi-ip>` with your Raspberry Pi’s IP address.

---

## API Endpoints

### REST

| Route       | Method | Description                  |
|-------------|--------|------------------------------|
| `/greet`    | GET    | Returns all greetings        |
| `/greet`    | POST   | Add a new greeting           |
| `/health`   | GET    | Simple health check          |

### SOAP

| Path           | Method | Description                      |
|----------------|--------|----------------------------------|
| `/soap`        | POST   | SOAP greeting method             |
| `/soap/?wsdl`  | GET    | SOAP WSDL (service definition)   |

> The SOAP method `say_hello(name)` returns a greeting based on the latest message stored.

---

## Example: REST

```bash
curl -X POST http://<pi-ip>:5000/greet \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, world!"}'
```

---

## Example: SOAP XML Payload

Use in Postman or the `/soap-ui` HTML form:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:hel="spyne.greetings.soap">
  <soapenv:Header/>
  <soapenv:Body>
    <hel:say_hello>
      <hel:name>Alice</hel:name>
    </hel:say_hello>
  </soapenv:Body>
</soapenv:Envelope>
```

---

## Database Seeding

On first run, `init.sql`:

- Creates the `greetings` table
- Inserts sample messages (including personalized ones)

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

## Future Ideas

- CI pipeline with GitHub Actions
- GitHub Container Registry (GHCR) publishing
- Pi-to-Pi GitOps deployment
- K3s / Kubernetes multi-node deployment
- Add tests using `pytest`
- Webhook-based auto-deploy
