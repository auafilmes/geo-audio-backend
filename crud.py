
from sqlalchemy.orm import Session
from . import models, schemas

def create_point(db: Session, point: schemas.PointCreate):
    db_point = models.Point(**point.dict())
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def get_points(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Point).offset(skip).limit(limit).all()
