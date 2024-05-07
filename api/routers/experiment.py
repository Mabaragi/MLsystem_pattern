from fastapi import APIRouter, Depends
from api.models import Experiment
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.database import Database
from api.views import experiment_view
from api.schemas.experiment_schema import CreateExperiment


router = APIRouter()


@router.get("/all", response_model=list[Experiment])
async def get_all_experiments(db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await experiment_view.get_all_experiments(db)


@router.get("/model-id/{model_id}", response_model=list[Experiment])
async def get_experiments(model_id: int, db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await experiment_view.get_experiments(model_id, db)
    pass


@router.post("/model-id/{model_id}", response_model=None)
async def create_experiment(model_id: int, experiment: CreateExperiment, db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await experiment_view.create_experiment(model_id, experiment, db)
