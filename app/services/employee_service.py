from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.employee import Employee

def create_employee(db: Session, emp_data):
    existing = db.query(Employee).filter(
        (Employee.employee_id == emp_data.employee_id) |
        (Employee.email == emp_data.email)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists")

    new_emp = Employee(**emp_data.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_all_employees(db: Session):
    return db.query(Employee).all()

def delete_employee(db: Session, emp_id: str):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
