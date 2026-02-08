from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy import func
from app.models.attendance import Attendance, AttendanceStatus
from app.models.employee import Employee


def mark_attendance(db: Session, data):
    employee = db.query(Employee).filter(
        Employee.employee_id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    attendance = Attendance(
        employee_id=employee.id,
        date=data.date,
        status=data.status
    )

    try:
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this date"
        )


def get_attendance_by_employee(db: Session, employee_code: str, date=None):
    employee = db.query(Employee).filter(
        Employee.employee_id == employee_code
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    query = db.query(Attendance).filter(
        Attendance.employee_id == employee.id
    )

    if date:
        query = query.filter(Attendance.date == date)

    return query.order_by(Attendance.date.desc()).all()


def get_present_days_count(db: Session, employee_code: str):
    employee = db.query(Employee).filter(
        Employee.employee_id == employee_code
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    count = db.query(func.count(Attendance.id)).filter(
        Attendance.employee_id == employee.id,
        Attendance.status == AttendanceStatus.Present
    ).scalar()

    return {
        "employee_id": employee_code,
        "total_present_days": count
    }


