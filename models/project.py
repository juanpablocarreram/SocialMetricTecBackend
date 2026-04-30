import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean, JSON, DateTime
from sqlalchemy.sql import func
from db.database import Base #

class ProjectAreas(str, enum.Enum):
    educacion = "educacion"
    salud = "salud"
    justicia_social = "justicia_social"
    medio_ambiente = "medio_ambiente"
    economia_circular = "economia_circular"
    tecnologia_social = "tecnologia_social"


class Project(Base):
    __tablename__ = "project"
    project_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    impact_area = Column(String(255), nullable=True) 
    cover_image_url = Column(String(2048), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    page = Column(JSON, nullable=True) 
    created_at = Column(DateTime, server_default=func.now())