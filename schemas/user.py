from pydantic import BaseModel, ConfigDict
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password_hash: str

class UserOut(UserBase):
    is_admin: bool
    model_config = ConfigDict(from_attributes=True)