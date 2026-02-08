from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.employee import Employee
from app.models.attendance import Attendance


def get_dashboard_summary(db: Session):
    total_employees = db.query(func.count(Employee.id)).scalar()
    total_attendance_records = db.query(func.count(Attendance.id)).scalar()

    return {
        "total_employees": total_employees,
        "total_attendance_records": total_attendance_records
    }
