# variacode-backend-challenge

### by isaiascardenas

This repository contains a Flask back-end application for the `PagerDuty Customer Success Group Innovation Team
Back End Take Home Exercise`. The setup includes 2 Docker images:

- python3.10: For the Flask app
- mysql.9.0.1: For the database

The project run using the configuration stored in the `docker-compose.yml` file

## Prerequisites

- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))

## Setup

First we need to setup the environment variables used by the Flask application.

1. Open a terminal.
2. Navigate to the `backend/` directory
3. Create a `.env` file and copy the `.env.example` content
4. Navigate to the root directory, you should see `docker-compose.yml` file
5. Run the following command:

   ```bash
   docker-compose up --build
   ```

6. Wait for the setup ...
7. The Flask application runs on [http://localhost:3000/](http://localhost:3000/)

### Environment Variables

We set environment variables to configure Python behavior:

- `PYTHONDONTWRITEBYTECODE`: Prevents Python from writing pyc files to disk.
- `PYTHONUNBUFFERED`: Ensures Python output is sent directly to terminal without buffering.

### API endpoints

The Flask backend application has the following endpoints:

- `/dashboard/services`:
