from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.database import Database
from api.views import project_view
from api.routers import model
from bson.objectid import ObjectId
from api.schemas.project_schema import Project, CreateProject

router = APIRouter()


@router.get("/project", response_model=list[Project])
async def get_projects(db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await project_view.get_projects(db)


@router.get("/project/{project_id}", response_model=Project)
async def get_project(project_id: int, db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await project_view.get_project(project_id, db)


@router.post("/project", response_model=None)
async def create_project(project: CreateProject, db: AsyncIOMotorDatabase = Depends(Database.get_database)):
    return await project_view.create_project(project, db)
