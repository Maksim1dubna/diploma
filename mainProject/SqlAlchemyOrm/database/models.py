from datetime import datetime
from sqlalchemy import Integer, DateTime, CHAR, String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column
from sqlalchemy.sql import func
class BaseClass(DeclarativeBase):
    pass
class Task(MappedAsDataclass, BaseClass):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, init=True)
    name: Mapped[str] = mapped_column(CHAR(100))
    description: Mapped[str] = mapped_column(String(500))
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), init=False)