import uuid
import enum
from sqlalchemy import Column, Date, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base 

class AttendanceStatus(str, enum.Enum):
    Present = "Present"
    Absent = "Absent"

class Attendance(Base):
    __tablename__ = "attendance"

    __table_args__ = (
        UniqueConstraint('employee_id', 'date', name='unique_attendance_per_day'),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), nullable=False)

 
