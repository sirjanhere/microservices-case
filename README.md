# Microservices Case - Deployment Guide

## Overview

This project demonstrates a simple microservices setup using FastAPI and Redis, Dockerized with Docker Compose. The application exposes APIs to test containerized microservices and Redis connection.

---

## Prerequisites

Before you begin, ensure the following are installed on your system:

* Docker Desktop (must be running)
* Docker Compose (usually included with Docker Desktop)
* Git (optional, for cloning repository)

Also ensure you have a Docker Hub account and are logged in.

```bash
docker login
```

If using web-based login, follow on-screen instructions and keep Docker Desktop open.

---

## Project Structure

```
microservices-case/
├── web/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml
```

---

## Step 1: Clone Repository

```bash
git clone https://github.com/<your-username>/microservices-case.git
cd microservices-case
```

If using someone else's repository, download or copy project files manually.

---

## Step 2: Build and Run Docker Containers

Make sure Docker Desktop is **open and running**.

Then run:

```bash
docker-compose up --build
```

If you see a warning:

```
attribute `version` is obsolete
```

It is just a warning and can be ignored.

If Redis fails to download initially, fix by running:

```bash
docker pull redis:7
```

Then again:

```bash
docker-compose up --build
```

---

## Step 3: Access Application

Once containers are running successfully, the app will be available at:

```
http://localhost:8000
```

Available endpoints:

* `GET /` - Home route to verify service
* `GET /visits` - Test Redis counter

---

## Step 4: Test Using Postman

Open Postman and test endpoints:

### Test 1: Home Route

* Method: GET
* URL: `http://localhost:8000/`
* Expected Response:

```json
"message": "web service up"
```

### Test 2: Redis Counter

* Method: GET
* URL: `http://localhost:8000/visits`
* Expected Response:

```json
{"visits": 1}
```

Each refresh increases the counter.

---

## Step 5: Build Docker Image Manually (Optional)

To manually build image:

```bash
docker build -t <dockerhub-username>/microservices-case:<tag> ./web
```

Example:

```bash
docker build -t superwoman99/microservices-case:24f2004829 ./web
```

---

## Step 6: Push Image to Docker Hub

Make sure you're logged in:

```bash
docker login
```

Push image:

```bash
docker push <dockerhub-username>/microservices-case:<tag>
```

Example:

```bash
docker push superwoman99/microservices-case:24f2004829
```

If you get `TLS handshake timeout`, try again.

---

## Step 7: Verify Containers

Check running containers:

```bash
docker ps
```

Check images:

```bash
docker images
```

---

## Stop and Clean Containers

To stop services:

```bash
docker-compose down
```

To clean unused images:

```bash
docker system prune -f
```

---

## Notes

* Keep Docker Desktop *always open* while building and running containers.
* Internet is required to pull Redis and base Python image.
* Replace `<dockerhub-username>` with your Docker Hub username.
* Tag (like `24f2004829`) can be your roll number if needed.

---

## Troubleshooting

| Error                         | Solution                          |
| ----------------------------- | --------------------------------- |
| `failed to fetch oauth token` | Login again: `docker login`       |
| `TLS handshake timeout`       | Retry push command                |
| Redis connection fail         | Check Docker Desktop is running   |
| App not opening on port 8000  | Check logs: `docker-compose logs` |

---
