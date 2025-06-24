from fastapi import FastAPI
import uvicorn

app  = FastAPI()


@app.get('/api/sensors')
def welcome():
    return "This is health check for ingestion services"


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)