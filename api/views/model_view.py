from motor.motor_asyncio import AsyncIOMotorDatabase
from api.models import Model
from api.schemas.model_schema import CreateModel
from api.views import project_view
from api.database import Database


async def get_models(project_id, db: AsyncIOMotorDatabase):
    await project_view.get_project(project_id, db)
    models = await db['projects'].aggregate([
        {"$match": {"id": project_id}},  # 프로젝트 찾기
        {"$lookup": {
            "from": "models",  # 조인할 컬렉션
            "localField": "id",  # 프로젝트 컬렉션의 조인 필드
            "foreignField": "project_id",  # 모델 컬렉션의 조인 필드
            "as": "models"  # 결과를 저장할 필드 이름
        }},
        {"$unwind": "$models"},  # 각 모델을 독립된 문서로 펼치기
        {"$replaceRoot": {"newRoot": "$models"}}  # 모델 문서를 루트로 이동
    ]).to_list(length=20)
    models = [Model(**model) for model in models]
    return models


async def create_model(project_id: int, model: CreateModel, db: AsyncIOMotorDatabase):
    print("creating model...")
    project = await project_view.get_project(project_id, db)
    model = model.model_dump()
    model["project_id"] = project["id"]
    model['id'] = await Database.increase_counter_id('model')
    await db["models"].insert_one(model)
