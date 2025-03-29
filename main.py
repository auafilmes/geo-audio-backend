
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import points, upload

from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(points.router)
app.include_router(upload.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
