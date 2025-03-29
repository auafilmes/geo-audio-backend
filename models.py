
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    radius = Column(Float)
    media_type = Column(String)
    media_url = Column(String)
    description = Column(String)
    language = Column(String)
