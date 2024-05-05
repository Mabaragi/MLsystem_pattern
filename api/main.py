from fastapi import FastAPI
from api.database import Database
from api.routers import project, model


app = FastAPI()


@app.on_event('startup')
async def startup():
    await Database.connect()


@app.on_event('shutdown')
async def shutdown():
    await Database.disconnect()


@app.get('/')
async def root():
    return {"message": "hellow world!"}

app.include_router(project.router, tags=['project'])
app.include_router(model.router, prefix='/project', tags=['model'])
