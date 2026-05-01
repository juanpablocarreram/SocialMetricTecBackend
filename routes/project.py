from fastapi import APIRouter, Depends, HTTPException,status,Response
from schemas.project import Project, ProjectFull
from schemas.user import UserOut
from crud.project import get_project_from_db, create_project_in_db, delete_project_in_db
from routes.deps import get_current_user_from_token
from db.database import get_db

router = APIRouter(prefix="/project", tags=["project"])

# --- Endpoints ---s
""" Ruta para obtener la pagina, todos los usuarios pueden ver la pagina del proyecto """
@router.get("/{id_project}", response_model=ProjectFull)
async def get_all_info_about_project(id_project: int, db = Depends(get_db)):
    project = await get_project_from_db(db,id_project)
    if project is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return project

""" Ruta para editar la pagina del proyecto, solo lideres asignados al proyecto pueden editar"""
@router.put("/{id_project}}")
async def edit_proyect_page(id_project:int):
    #Logica para editar la pagina del proyecto
    pass

""" Ruta para crear un nuevo proyecto, solo lideres pueden crear proyectos """
@router.post("/create", response_model=ProjectFull)
async def create_project(project_info:Project,db = Depends(get_db),user : UserOut = Depends(get_current_user_from_token)):
    created_project = create_project_in_db(db,project_info,user)
    return created_project

""" Ruta para eliminar un proyecto existente, solo un lider relacionado al proyecto puede eliminarlo o un admin"""
@router.delete("/{project_id}/delete")
def delete_project(project_id: int, db = Depends(get_db), user:UserOut = Depends(get_current_user_from_token)):
        result = delete_project_in_db(db, project_id, user)
        if result == "no_encontrado":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="El proyecto no existe."
            )
        if result == "acceso_denegado":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="No tienes permiso para eliminar este proyecto."
            )
        # Éxito: 200 OK
        return {"message": "Proyecto eliminado exitosamente", "project_id": project_id}
        
""" Ruta para listar los proyectos, su nombre, descripcion e imagen de preview """
@router.get("/listpreview")
async def list_projects_preview():
    pass
