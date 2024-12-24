from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, database
import shutil

img_router = APIRouter()

@img_router.post("/images/")
def upload_image(
    image: schemas.ImageCreate,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(database.get_db),
):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    image.image_path = file_path
    return crud.create_image(db, image)
