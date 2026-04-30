from sqlalchemy.orm import Session
from models.project import Project
from schemas.project import Project as ProjectSchema
""" Hace la query a la base de datos que retorna el registro con todo el proyecto """
def get_project_from_db(db: Session, id_project: int):
    return db.query(Project).filter(Project.project_id == id_project).first()
""" Hace la insercion en la base de datos de un proyecto con la informacion """
def create_project_in_db(db: Session,project_info: ProjectSchema):
    new_project = Project(
        project_name = project_info.project_name, # Antes era 'name'
        description = project_info.description,
        impact_area = project_info.impact_area,
        cover_image_url = project_info.cover_image_url, 
        is_active = True
    )
    db.add(new_project) # Lo metes al "carrito"
    db.commit()            # Guardas en la base de datos
    db.refresh(new_project)
    return new_project