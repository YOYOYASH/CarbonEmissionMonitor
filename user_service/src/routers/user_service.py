from fastapi import APIRouter, HTTPException, status

from src.services.password_service import  hash_password

import src.schemas  as schemas

user = APIRouter(prefix='/users',tags=['users'])


@user.post("",status_code= status.HTTP_201_CREATED,response_model=schemas.DisplayUser)
async def create_user(user_data: schemas.CreateUser):
    try:
        hashed_password = hash_password(user_data.password)
        print(hashed_password)
        return user_data
    except HTTPException as http_exec:
        raise http_exec
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

