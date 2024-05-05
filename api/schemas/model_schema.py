from pydantic import BaseModel, Field
from datetime import datetime


class Project(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="첫 번째 프로젝트")
    description: str = Field(example="프로젝트 내용")
    created_at: datetime = Field(default_factory=datetime.now, example=datetime.utcnow())


class GetProject(BaseModel):
    id: int = Field(example=1)


class CreateModel(BaseModel):
    name: str = "모델 이름을 입력해주세요"
    description: str = "모델 내용을 입력해주세요"
    created_at: datetime = Field(default_factory=datetime.now)
