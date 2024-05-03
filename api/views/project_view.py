from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.database import Database
from api.models import Project


async def get_projects(db: AsyncIOMotorDatabase):
    projects = await db['projects'].find().to_list(length=20)
    projects = [Project(**project) for project in projects]
    return projects


async def get_project(project_id, db: AsyncIOMotorDatabase, ):
    project = await db['projects'].find_one({'_id': ObjectId(project_id)})
    return project


async def create_project(db: AsyncIOMotorDatabase):
    Project.id = await Database.increase_counter_id('project')
    project = Project().model_dump()
    await db["projects"].insert_one(project)


