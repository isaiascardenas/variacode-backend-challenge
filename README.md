# variacode-backend-challenge

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

## Environment Variables

The `.env.example` includes the following environment variables:

- `FLASK_APP`: Flask application name
- `FLASK_ENV`: Environment, util for debug mode
- `FLASK_RUN_PORT`: Port configuration for Flask app
- `FLASK_RUN_HOST`: Host configuration for Flask app
- `DATABASE_HOST`: Database host configuration
- `DATABASE_PORT`: Database port configuration
- `DATABASE_NAME`: Database name configuration
- `DATABASE_USER`: Database user access configuration
- `DATABASE_PASSWORD`: Database password access configuration
- `DATABASE_ECHO`: Database echo mode, for queries debug mode
- `PAGER_DUTY_API_KEY`: Pager Duty api key, for database seeder
- `PAGER_DUTY_API_ENDPOINT`: Pager Duty API endpoint, for database seeder

## API endpoints

The Flask backend application has the following endpoints:

### Services

List all Services

```http
GET /dashboard/services
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |


```javascript
{
  "total" : integer,
  "services" : array,
}
```

The `total` attribute contains the total records.

The `services` attribute contains the Services array.

### Services with Incidents

List all Services with their related Incidents

```http
GET /dashboard/services/incidents
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |


```javascript
{
  "total" : integer,
  "services" : array,
}
```

The `total` attribute contains the total records.

The `services` attribute contains the Services array.

### Incidents

List all Incidents filtered by `status` or `service_id`

```http
GET /dashboard/incidents?search_by={value}&search_value={value}
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|  `search_by` | `string` |  **Optional**. Allowed values: `status`, `service_id` |
|  `search_value` | `string` |  **Optional**. An Incident's status or a Service id |


```javascript
{
  "total" : integer,
  "incidents" : array,
}
```

The `total` attribute contains the total records.

The `incidents` attribute contains the Incidents array.

### Teams with Services

List all Teams with their related Services

```http
GET /dashboard/teams/services
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |

```javascript
{
  "total" : integer,
  "teams" : array,
}
```

The `total` attribute contains the total records.

The `teams` attribute contains the Teams array.

### Escalation Policies

List all Escalation policies with their related Teams and Services

```http
GET /dashboard/escalation_policies
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |

```javascript
{
  "total" : integer,
  "escalation_policies" : array,
}
```

The `total` attribute contains the total records.

The `escalation_policies` attribute contains the Escalation policies array.


### Services report

CSV report for all Services

```http
GET /reports/services
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |


Response: `csv file`

### Services with Incidents report

CSV report for all Services with their related Incidents

```http
GET /reports/services/incidents
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |


Response: `csv file`

### Incidents report

CSV report for all Incidents filtered by `status` or `service_id`

```http
GET /reports/incidents?search_by={value}&search_value={value}
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|  `search_by` | `string` |  **Optional**. Allowed values: `status`, `service_id` |
|  `search_value` | `string` |  **Optional**. An Incident's status or a Service id |


Response: `csv file`

### Teams with Services report

CSV report for all Teams with their related Services

```http
GET /reports/teams/services
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |

Response: `csv file`


### Escalation Policies report

CSV report for all Escalation policies with their related Teams and Services

```http
GET /reports/escalation_policies
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
|           |      |             |

Response: `csv file`


<br/>
<br/>
<i>by isaiascardenas</i>
