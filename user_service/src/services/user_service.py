from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User
from src.schemas import CreateUser,DisplayUser, TokenData
from src.dependencies.database import get_db
from services.password_service import hash_password, verify_password
from src.services.oauth2 import create_access_token


async def create_user(user_data: CreateUser,db:AsyncSession) -> DisplayUser:
    try:
        existing_user = (await db.scalars(select(User).where(User.email == user_data.email or User.username == user_data.username))).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="User already exists"
            )
        hashed_password = hash_password(user_data.password)
        user_data.password = hashed_password
        print(hashed_password)
        user = User(**user_data.model_dump())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    except HTTPException as http_exec:
        raise http_exec
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


async def verify_user_and_create_token(user_credentials: OAuth2PasswordRequestForm,db:AsyncSession):
    try:
        # user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
        user = (await db.scalars(select(User).where(User.username == user_credentials.username))).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")
        if not verify_password(user.password,user_credentials.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")
        access_token = create_access_token({"sub":user.username,"role":user.role})
        return TokenData(token=access_token,type='bearer')
    except HTTPException as http_exec:
        raise http_exec
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))