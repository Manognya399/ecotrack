# EcoTrack — Supply Chain Sustainability Dashboard

Built for SC1 problem statement.

## Setup

### Backend
cd backend
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload

### Frontend
cd frontend
npm install
npm run dev

## Team
- Person 1: Backend APIs
- Person 2: Frontend Dashboard  
- Person 3: Scoring Engine
- Person 4: Database & Setup

## API Endpoints
- GET /vendors — list all vendors
- POST /vendors — add vendor
- GET /vendors/{id}/carbon-score — get score
- GET /dashboard/summary — overall stats
- GET /shipments — list shipments
