
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/points/", response_model=schemas.Point)
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    return crud.create_point(db=db, point=point)

@router.get("/points/", response_model=list[schemas.Point])
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_points(db=db, skip=skip, limit=limit)
