import enum
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from schemas.page import Page

class ProjectAreas(str, enum.Enum):
    educacion = "educacion"
    salud = "salud"
    justicia_social = "justicia_social"
    medio_ambiente = "medio_ambiente"
    economia_circular = "economia_circular"
    tecnologia_social = "tecnologia_social"

class Project(BaseModel):
    # Usamos project_name para que coincida con el SQL
    project_name: str 
    description: Optional[str] = None
    impact_area: ProjectAreas
    cover_image_url: str
    is_active: bool = True
class ProjectFull(Project):
    # Campos que genera la base de datos
    project_id: int
    created_at: datetime 
    page:Page# O usar tu clase Page si ya la tienes
    model_config = ConfigDict(from_attributes=True) # Para Pydantic v2