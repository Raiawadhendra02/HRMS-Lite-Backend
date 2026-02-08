from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models.attendance import Attendance
from app.models.employee import Employee


def mark_attendance(db: Session, data):
    """
    Mark attendance for an employee.
    Prevent duplicate attendance for the same date.
    """

    # Check if employee exists
    employee = db.query(Employee).filter(
        Employee.employee_id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # Create attendance record
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


def get_attendance_by_employee(db: Session, employee_code: str):
    """
    Get all attendance records for a specific employee.
    """

    # Check if employee exists
    employee = db.query(Employee).filter(
        Employee.employee_id == employee_code
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    records = db.query(Attendance).filter(
        Attendance.employee_id == employee.id
    ).order_by(Attendance.date.desc()).all()

    return records

