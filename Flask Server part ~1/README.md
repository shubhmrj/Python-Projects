# Python Project Hub

A web platform where users can sign up, log in, view all your Python projects, read their descriptions and code, and run them in real time.

## Features
- User authentication (signup & login)
- List Python projects with description and code
- Run Python code in real time from the browser

## Tech Stack
- Frontend: React
- Backend: FastAPI (Python)
- Database: SQLite

## Getting Started

### Backend
1. Navigate to `backend` and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to `frontend` and install dependencies:
   ```bash
   npm install
   ```
2. Run the frontend:
   ```bash
   npm start
   ```

---

### Security Note
Do NOT deploy this as-is for public use. Running arbitrary code is dangerous. Use containers, resource limits, and input validation for real deployments.
