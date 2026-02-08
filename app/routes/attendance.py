from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services import attendance_service
from app.schemas.attendance import AttendanceCreate, AttendanceResponse

router = APIRouter(prefix="/api/attendance", tags=["Attendance"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Mark Attendance
@router.post("/", status_code=201, response_model=AttendanceResponse)
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    return attendance_service.mark_attendance(db, data)


# Get Attendance By Employee
@router.get("/{employee_id}", status_code=200, response_model=list[AttendanceResponse])
def get_attendance(employee_id: str, db: Session = Depends(get_db)):
    return attendance_service.get_attendance_by_employee(db, employee_id)

