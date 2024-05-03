from fastapi import APIRouter, Depends
from api.models import Model
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.database import Database
from api.views import model_view

router = APIRouter()


@router.get("/model", response_model=list[Model])
async def get_project(db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await model_view.get_models(db)


@router.post("/model", response_model=None)
async def create_project(db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await model_view.create_model(db)
