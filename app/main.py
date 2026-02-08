from fastapi import FastAPI
from app.database import Base, engine

# Import models so tables are registered
from app.models import employee, attendance

from app.routes import employee as employee_routes
from app.routes import attendance as attendance_routes

app = FastAPI(title="HRMS Lite API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(employee_routes.router)
app.include_router(attendance_routes.router)

