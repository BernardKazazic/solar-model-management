from pydantic import BaseModel, field_validator
from typing import List, Any
import json


class UploadSuccessResponse(BaseModel):
    message: str
    model_id: int


class ModelResponse(BaseModel):
    id: int
    name: str
    type: str
    version: int
    features: Any
    plant_name: str
    is_active: bool
    file_type: str

    @field_validator("features")
    @classmethod
    def parse_features(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return v
        return v


class ActiveModelResponse(BaseModel):
    id: int
    features: Any
    plant_id: int
    file_type: str

    @field_validator("features")
    @classmethod
    def parse_features(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return v
        return v


class PowerPlantDetailResponse(BaseModel):
    id: int
    name: str
    latitude: float | None
    longitude: float | None
    capacity: float | None
    model_count: int


class PowerPlantResponse(BaseModel):
    id: int
    longitude: float | None
    latitude: float | None
    capacity: float | None


class ModelsListResponse(BaseModel):
    models: List[ModelResponse]
    total_count: int
    page: int
    page_size: int
    total_pages: int


class ModelUpdateRequest(BaseModel):
    features: List[str]
    is_active: bool


class UpdateSuccessResponse(BaseModel):
    message: str
    model_id: int


class DeleteSuccessResponse(BaseModel):
    message: str


class AvailableFeaturesResponse(BaseModel):
    features: List[str]
