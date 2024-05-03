from motor.motor_asyncio import AsyncIOMotorDatabase
from api.models import Model


async def get_models(db: AsyncIOMotorDatabase):
    models = await db['models'].find().to_list(length=20)
    models = [Model(**model) for model in models]
    return models


async def create_model(db: AsyncIOMotorDatabase):
    model = Model().model_dump()
    await db["models"].insert_one(model)
