from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
import uvicorn

from src.routers import user,auth
from src.dependencies.database import sessionmanger

app = FastAPI()


app.include_router(user.user,prefix="/api/users")
app.include_router(auth.auth,prefix="/api/users")



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if sessionmanger._engine is not None:
        await sessionmanger.close() 


@app.get('/welcome')
async def health_check():
    return "This is health check api for user service"


if  __name__ == "__main__" :
    uvicorn.run(app,host="127.0.0.1",port=8080)












