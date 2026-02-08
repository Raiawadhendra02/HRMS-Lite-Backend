from fastapi import FastAPI
from app.database import Base, engine

from app.models import employee, attendance

from app.routes import employee as employee_routes
from app.routes import attendance as attendance_routes
from app.routes import dashboard as dashboard_routes

app = FastAPI(title="HRMS Lite API")

Base.metadata.create_all(bind=engine)

app.include_router(employee_routes.router)
app.include_router(attendance_routes.router)
app.include_router(dashboard_routes.router)


