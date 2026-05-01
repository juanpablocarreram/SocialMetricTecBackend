from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from models.project import Project, Manages
from schemas.project import Project as ProjectSchema
from schemas.user import UserOut as UserOutSchema

""" Hace la query a la base de datos que retorna el registro con todo el proyecto """
def get_project_from_db(db: Session, id_project: int):
    return db.query(Project).filter(Project.project_id == id_project).first()

""" Hace la insercion en la base de datos de un proyecto con la informacion """
def create_project_in_db(db: Session,project_info: ProjectSchema,user: UserOutSchema):
    try:
        new_project = Project(
            project_name = project_info.project_name,
            description = project_info.description,
            impact_area = project_info.impact_area,
            cover_image_url = project_info.cover_image_url, 
            is_active = True
        )
        db.add(new_project)
        db.flush() 

        new_manage = Manages(
            username = user.username,
            project_id = new_project.project_id
        )
        db.add(new_manage)
        
        db.commit() # Aquí se hacen permanentes AMBOS
        db.refresh(new_project)
        return new_project
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El proyecto con el nombre '{project_info.project_name}' ya existe."
        )
    except Exception as e:
        db.rollback() # Si algo falló arriba, cancela TODO lo pendiente
        raise e # Lanza el error para que FastAPI lo maneje
""" Elimina un proyecto que si existe en la base """
def delete_project_in_db(db: Session, project_id:int, current_user:UserOutSchema):
    db_project = db.query(Project).filter(Project.project_id == project_id).first()
    if not db_project:
        return "no_encontrado"
    # Verificar permisos
    # Comprobamos si el usuario es administrador O si está en la tabla 'manages' para este proyecto
    is_manager = db.query(Manages).filter(
        Manages.project_id == project_id, 
        Manages.username == current_user.username
    ).first()

    if not current_user.is_admin and not is_manager:
        return "acceso_denegado"

    # Proceder con la eliminación
    # Gracias al ON DELETE CASCADE en tu SQL, esto borra:
    # El proyecto + filas en manages + métricas + beneficiarios + tags asociados.
    try:
        db.delete(db_project)
        db.commit()
        return "exito"
    except Exception as e:
        db.rollback()
        raise e