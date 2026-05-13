# Fullstack Railway CI/CD Lab

## Components
- Frontend: React + Vite
- Backend: Flask REST API
- Database: PostgreSQL on Railway
- CI: GitHub Actions
- CD: Railway

## Backend endpoints
- GET `/api/data`
- POST `/api/data`
- DELETE `/api/data/:id`

## Railway variables
Backend:
- `DATABASE_URL` = reference from PostgreSQL service
- `PORT` = `5000`

Frontend:
- `VITE_API_URL` = public backend URL from Railway
