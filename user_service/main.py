from fastapi import FastAPI, Request, Response
import uvicorn

from src.routers import user_service

app = FastAPI()


app.include_router(user_service.user)


@app.get('/welcome')
async def health_check():
    return "This is health check api for user service"


if  __name__ == "__main__" :
    print(True)
    uvicorn.run(app,host="127.0.0.1",port=8080)












