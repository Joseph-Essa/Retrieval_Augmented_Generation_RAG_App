from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId
from datetime import datetime


class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: int = Field(..., gt=0, description="Unique project ID")
    
    # created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    # updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")

    @validator('project_id')
    def validate_project_id(cls, value):
        if not str(value).isalnum():
            raise ValueError('Project_id must be alphanumeric')
        return value

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        validate_by_name = True

    @classmethod
    def get_indexes(cls):
        return [
            {
                "key": [("project_id", 1)],
                "name": "Project_id_index_1",
                "unique": True
            }
        ]
