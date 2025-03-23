# Flask API + MariaDB (Raspberry Pi Project)

A simple full-stack API project built with Flask and MariaDB — containerized using Docker Compose and deployable to a Raspberry Pi. Includes a dashboard, secure environment handling, and auto-seeded database.

Using as I brush up on some skills with my Raspberry Pi.

---

## Features

- REST API built with Flask
- Data stored in MariaDB
- Containerized with Docker Compose
- `.env` support for secure credentials
- Auto-creates & seeds a greetings table
- HTML dashboard to view messages
- Tested on Raspberry Pi

---

## Setup

### 1. Clone the Repo

Clone using SSH:

```bash
git clone git@github.com:mbulkeley/flask-api.git
cd flask-api
```
Or clone using HTTPS:

git clone https://github.com/mbulkeley/flask-api.git


### 2. Create a `.env` File

```env
MYSQL_ROOT_PASSWORD=yourpassword
MYSQL_DATABASE=flaskdb
MYSQL_USER=flaskuser
MYSQL_PASSWORD=yourpassword
DB_HOST=db
```

> **Do not commit `.env`** — it's listed in `.gitignore`.

---

### 3. Run It

```bash
docker compose up --build
```

### 4. Visit the Dashboard

Open your browser:

```
http://<pi-ip>:5000/
```

---

## API Endpoints

| Route       | Method | Description                  |
|-------------|--------|------------------------------|
| `/greet`    | GET    | Returns all greetings        |
| `/greet`    | POST   | Add a new greeting           |
| `/health`   | GET    | Simple health check          |
| `/`         | GET    | HTML dashboard               |

### Example:

```bash
curl -X POST http://<pi-ip>:5000/greet \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, world!"}'
```

---

## Database Seeding

On first run, the `init.sql` file:

- Creates the `greetings` table
- Inserts example messages

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

## Future Ideas

- GitHub Actions CI pipeline
- Publish to GitHub Container Registry (GHCR)
- K3s Kubernetes deployment on Raspberry Pi cluster
