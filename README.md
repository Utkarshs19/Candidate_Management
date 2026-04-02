# Candidate Management API

A simple FastAPI backend to manage recruitment candidates.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

API docs available at: http://127.0.0.1:8000/docs

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/candidates` | Add a new candidate |
| GET | `/candidates` | List all candidates (optional `?status=` filter) |
| PUT | `/candidates/{id}/status` | Update a candidate's status |

## Example Requests

### Create a candidate
```bash
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","skill":"Python","status":"applied"}'
```

### Get all candidates
```bash
curl http://localhost:8000/candidates
```

### Filter by status
```bash
curl http://localhost:8000/candidates?status=interview
```

### Update status
```bash
curl -X PUT http://localhost:8000/candidates/{id}/status \
  -H "Content-Type: application/json" \
  -d '{"status":"interview"}'
```

## Valid statuses
`applied` | `interview` | `selected` | `rejected`
