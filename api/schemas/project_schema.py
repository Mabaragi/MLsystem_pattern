from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

from typing import Any
from pydantic_core import CoreSchema, core_schema
from pydantic import GetCoreSchemaHandler

#
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_pydantic_core_schema__(
#         cls, source_type: Any, handler: GetCoreSchemaHandler
#     ) -> CoreSchema:
#         return core_schema.no_info_after_validator_function(cls, handler(str))
#


class Project(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="첫 번째 프로젝트")
    description: str = Field(example="프로젝트 내용")
    created_at: datetime = Field(default_factory=datetime.now, example=datetime.utcnow())


class GetProject(BaseModel):
    id: int = Field(example=1)


class CreateProject(BaseModel):
    name: str = "프로젝트 이름을 입력해주세요"
    description: str = "프로젝트 내용을 입력해주세요"
    created_at: datetime = Field(default_factory=datetime.now)
