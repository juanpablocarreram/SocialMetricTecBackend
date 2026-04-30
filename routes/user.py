from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserLogin, UserOut
from routes.deps import get_current_user_from_token, get_admin_user
from crud.user import insert_user_to_db

router = APIRouter(prefix="/user", tags=["user"])

# --- Endpoints ---
# Solo admins pueden registrar
@router.post("/register", dependencies=[Depends(get_admin_user)])
async def register(user: UserCreate):
    # Aquí guardarías en DB con await
    await insert_user_to_db(user)
    return {"message": f"Usuario {user.username} creado por el administrador"}

@router.post("/login")
async def login(user: UserLogin):
    return {"token": "tu_jwt_generado"}

@router.get("/me")
async def read_current_user(current_user: UserOut = Depends(get_current_user_from_token)):
    return current_user