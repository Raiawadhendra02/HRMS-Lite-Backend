from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from app.database import SessionLocal
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.services import attendance_service

router = APIRouter(prefix="/api/attendance", tags=["Attendance"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", status_code=201, response_model=AttendanceResponse)
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    return attendance_service.mark_attendance(db, data)


@router.get("/{employee_id}", response_model=list[AttendanceResponse])
def get_attendance(
    employee_id: str,
    date: date | None = Query(default=None),
    db: Session = Depends(get_db)
):
    return attendance_service.get_attendance_by_employee(db, employee_id, date)


@router.get("/summary/{employee_id}")
def get_present_summary(employee_id: str, db: Session = Depends(get_db)):
    return attendance_service.get_present_days_count(db, employee_id)


