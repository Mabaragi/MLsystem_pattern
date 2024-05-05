from fastapi import APIRouter, Depends
from api.models import Model
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.database import Database
from api.views import model_view
from api.schemas.model_schema import CreateModel


router = APIRouter()


@router.get("/{project_id}/model", response_model=list[Model])
async def get_models(project_id: int, db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await model_view.get_models(project_id, db)


@router.post("/{project_id}/model", response_model=None)
async def create_model(project_id: int, model: CreateModel, db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await model_view.create_model(project_id, model, db)