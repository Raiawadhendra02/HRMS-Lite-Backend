from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.employee import EmployeeCreate
from app.services import employee_service

router = APIRouter(prefix="/api/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return employee_service.create_employee(db, emp)

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return employee_service.get_all_employees(db)

@router.delete("/{emp_id}", status_code=200)
def delete_employee(emp_id: str, db: Session = Depends(get_db)):
    employee_service.delete_employee(db, emp_id)
    return {"message": "Employee deleted successfully"}
