
import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

UPLOAD_DIRECTORY = "static"

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)

    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    return JSONResponse(content={"filename": file.filename, "url": f"/static/{file.filename}"})
