from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine

from app.models import employee, attendance
from app.routes import employee as employee_routes
from app.routes import attendance as attendance_routes
from app.routes import dashboard as dashboard_routes

app = FastAPI(title="HRMS Lite API")

# ---------------- CORS FIX ----------------
origins = [
    "http://localhost:5173",  # React local
    "http://localhost:3000",
    "https://your-frontend-url.onrender.com"  # later for deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------------------------

Base.metadata.create_all(bind=engine)

app.include_router(employee_routes.router)
app.include_router(attendance_routes.router)
app.include_router(dashboard_routes.router)


