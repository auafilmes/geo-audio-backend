
from pydantic import BaseModel

class PointBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    radius: float
    media_type: str
    media_url: str
    description: str
    language: str

class PointCreate(PointBase):
    pass

class Point(PointBase):
    id: int

    class Config:
        orm_mode = True
