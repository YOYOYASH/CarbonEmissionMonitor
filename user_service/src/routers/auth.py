from fastapi import APIRouter,status,Depends,HTTPException,Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated

from src.services.user_service import verify_user_and_create_token
from dependencies.database import get_db

auth = APIRouter()

@auth.post('/login')
async def login_user(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()],db:AsyncSession = Depends(get_db)):
    try:
        return await verify_user_and_create_token(user_credentials,db)
    except HTTPException as http_exec:
        raise http_exec
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))