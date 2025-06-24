from pydantic import BaseModel, EmailStr



class UserBase(BaseModel):
    username:str
    email: EmailStr
    password:str

class CreateUser(UserBase):
    present_company: str
    role:str

class DisplayUser(BaseModel):
    id:int
    username: str
    email:str
    present_company:str
    role:str

    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    email:EmailStr


class TokenData(BaseModel):
    token:str
    type:str