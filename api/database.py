from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure


class Database:
    _client: AsyncIOMotorClient = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            raise Exception("Database not initialized")
        return cls._client

    @classmethod
    def get_database(cls, database_name: str = "fastapi_db"):
        client = cls.get_client()
        return client[database_name]

    @classmethod
    async def connect(cls, uri="mongodb://mongodb:27017"):
        if cls._client is None:
            try:
                cls._client = AsyncIOMotorClient(uri)
                await cls._client.admin.command('ping')
                print("Connected to")
            except ConnectionFailure:
                print("Failed to connect to MongoDB")
                raise ConnectionFailure("Could not connect to MongoDB")

    @classmethod
    async def disconnect(cls):
        if cls._client is not None:
            await cls._client.close()
            print("Disconnected from MongoDB")

    @classmethod
    async def increase_counter_id(cls, collection_name: str):
        database = cls.get_database()
        collection = database["counter_id"]

        document = await collection.find_one({"collection_name": collection_name})
        if document is None:
            await collection.insert_one({"collection_name": collection_name, "counter": 1})
            counter_id = 1
        else:
            counter_id = document["counter"] + 1
            await collection.update_one({"collection_name": collection_name}, {"$inc": {"counter": 1}})

        return counter_id
