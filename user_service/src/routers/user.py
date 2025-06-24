import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.user_service import create_user

from dependencies.database import get_db

import src.schemas  as schemas


user = APIRouter(tags=['users'])


@user.post("",status_code= status.HTTP_201_CREATED,response_model=schemas.DisplayUser)
async def create_user_route(user_data: schemas.CreateUser,db:AsyncSession = Depends(get_db)):
    try:
       created_user = await create_user(user_data,db)
       return created_user
    except HTTPException as http_exec:
        raise http_exec
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

