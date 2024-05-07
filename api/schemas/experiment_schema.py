from pydantic import BaseModel, Field
from datetime import datetime


class GetProject(BaseModel):
    id: int = Field(example=1)


class CreateExperiment(BaseModel):
    model_version_id: str = "some model version"
    parameters: dict = Field(default_factory=dict)
    training_dataset: str = "some training dataset"
    validation_dataset: str = "some validation dataset"
    test_dataset: str = "some test dataset"
    evaluations: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)