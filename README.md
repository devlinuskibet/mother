Take your time to read and understand this:


🧠 MamaCare – Local Setup Instructions
1. Prerequisites

Before running the project, ensure you have:

Python 3.10 or 3.11
Node.js (LTS version recommended)
npm (comes with Node.js)
Git
PostgreSQL or SQLite (SQLite works out of the box)

Optional but helpful:

VS Code
Python virtual environment tool (venv)
2. Clone the Repository
git clone https://github.com/devlinuskibet/mother.git
cd mother
3. Project Structure Overview
mamacare-backend/   → FastAPI backend
mamacare-frontend/  → React frontend (Vite)
🖥️ Backend Setup (FastAPI)
4. Navigate to backend
cd mamacare-backend
5. Create virtual environment
Windows:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python3 -m venv venv
source venv/bin/activate
6. Install dependencies
pip install -r requirements.txt
7. Environment variables

Create a .env file:

cp .env.example .env

Then edit .env and fill in:

DATABASE_URL=sqlite:///./mamacare.db
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_key_if_used
PINECONE_API_KEY=your_key_if_used
8. Run backend server
uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000

API docs:

http://127.0.0.1:8000/docs
🌐 Frontend Setup (React + Vite)
9. Open new terminal and navigate
cd mamacare-frontend
10. Install dependencies
npm install
11. Configure environment variables

Create a .env file:

VITE_API_URL=http://127.0.0.1:8000/api
12. Start frontend
npm run dev

Frontend runs at:

http://localhost:5173
🔗 Connecting Frontend + Backend

Ensure:

Backend: http://127.0.0.1:8000
Frontend: http://localhost:5173
Frontend uses VITE_API_URL for all requests
🧪 First Run Checklist

After setup, test:

Backend
http://127.0.0.1:8000/docs
Frontend
Login page loads
Signup works
Dashboard loads
API test
/api/auth/login
/api/prediction/predict
/api/chat/chat
⚠️ Common Issues
1. Module not found

Fix:

pip install -r requirements.txt
2. Port already in use

Change port:

uvicorn app.main:app --reload --port 8001
3. Frontend API errors

Check .env:

VITE_API_URL=http://127.0.0.1:8000/api
🚀 Optional Production Notes

When deploying:

Backend → Render / Railway
Frontend → Vercel / Netlify
Replace localhost URLs with deployed backend URL