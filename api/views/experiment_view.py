from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from api.models import Experiment
from api.schemas.experiment_schema import CreateExperiment
from api.views import project_view, model_view
from api.database import Database


async def get_all_experiments(db: AsyncIOMotorDatabase):
    print("getting all experiments")
    experiments = await db['experiments'].find().to_list(length=20)
    print(experiments)
    experiments = [Experiment(**experiment) for experiment in experiments]
    return experiments


async def get_experiments(model_id, db: AsyncIOMotorDatabase):
    await model_view.get_model(model_id, db)
    experiments = await db['models'].aggregate([
        {"$match": {"id": model_id}},  # 프로젝트 찾기
        {"$lookup": {
            "from": "experiments",  # 조인할 컬렉션
            "localField": "id",  # 프로젝트 컬렉션의 조인 필드
            "foreignField": "model_id",  # 모델 컬렉션의 조인 필드
            "as": "experiments"  # 결과를 저장할 필드 이름
        }},
        {"$unwind": "$experiments"},  # 각 모델을 독립된 문서로 펼치기
        {"$replaceRoot": {"newRoot": "$experiments"}}  # 모델 문서를 루트로 이동
    ]).to_list(length=20)
    if not experiments:
        raise HTTPException(status_code=404, detail="Experiment not found")
    experiments = [Experiment(**experiment) for experiment in experiments]
    print(experiments)
    return experiments


async def create_experiment(model_id: int, experiment: CreateExperiment, db: AsyncIOMotorDatabase):
    # print("creating experiment..")
    # project = await model_view.get_model(model_id, db)
    # model = model.model_dump()
    # model["model_id"] = project["id"]
    # model['id'] = await Database.increase_counter_id('model')
    await model_view.get_model(model_id, db)  # 모델이 존재하는지 확인
    experiment = experiment.model_dump()
    experiment['model_id'] = model_id
    experiment['id'] = await Database.increase_counter_id("experiments")
    await db['experiments'].insert_one(experiment)
    return
