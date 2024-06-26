from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

from typing import Any
from pydantic_core import CoreSchema, core_schema
from pydantic import GetCoreSchemaHandler


class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))


class Project(BaseModel):
    id: int
    name: str = "프로젝트 이름"
    description: str = "상세 사항"
    created_at: datetime = Field(default_factory=datetime.now)


class Model(BaseModel):
    project_id: int
    id: int
    name: str = "모델 이름"
    description: str = "모델 상세"
    created_at: datetime = Field(default_factory=datetime.now)


class Experiment(BaseModel):
    model_id: int
    id: int
    model_version_id: str = "some model version"
    parameters: dict = Field(default_factory=dict)
    training_dataset: str = "some training dataset"
    validation_dataset: str = "some validation dataset"
    test_dataset: str = "some test dataset"
    evaluations: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)