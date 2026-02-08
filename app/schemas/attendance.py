from pydantic import BaseModel
from datetime import date
from uuid import UUID
from app.models.attendance import AttendanceStatus


class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: AttendanceStatus


class AttendanceResponse(BaseModel):
    id: UUID
    employee_id: UUID
    date: date
    status: AttendanceStatus

    class Config:
        orm_mode = True


