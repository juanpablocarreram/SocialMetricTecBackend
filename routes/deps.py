from fastapi import Depends, HTTPException, status
from schemas.user import UserOut
async def get_current_user_from_token():
    # Aquí iría tu lógica de decodificar el JWT que vimos antes
    """ await fake_async_db_call()  """ # Simula una llamada a DB
    # Por ahora simulamos un usuario recuperado de la DB
    user_mock = UserOut(username="admin_juan", mail="juan@tec.mx", es_admin=True)
    return user_mock

# 2. Esta usa la anterior para verificar permisos
async def get_admin_user(current_user: UserOut = Depends(get_current_user_from_token)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos suficientes."
        )
    return current_user
