from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.database import Database
from api.models import Project
from api.schemas import project_schema


async def get_projects(db: AsyncIOMotorDatabase):
    projects = await db['projects'].find().to_list(length=20)
    projects = [Project(**project) for project in projects]
    return projects


async def get_project(project_id: int, db: AsyncIOMotorDatabase):
    try:
        project = await db['projects'].find_one({'id': project_id})
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Database operation failed")
    if not project:
        print("project not found")
        raise HTTPException(status_code=404, detail="Project not found")
    return project


async def create_project(project: project_schema.CreateProject, db: AsyncIOMotorDatabase):
    project = project.model_dump()
    project['id'] = await Database.increase_counter_id('project')
    await db["projects"].insert_one(project)

