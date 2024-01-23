from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, UploadFile  # for image uploads
from sqlalchemy.orm import Session
from uuid import uuid4 as gen_unique_name

from app.schema.skills import SkillCreate, SkillPublic
from app.dependencies import get_db
from app import crud

IMAGE_FILE_PATH = "static/images"

router = APIRouter()

@router.post("/users/{user_id}/skills/", response_model=SkillPublic, tags=["skills"])
def create_skill_for_user_using_id(user_id: int, skill: SkillCreate, db: Session = Depends(get_db)):
    user_exists = crud.get_user_by_id(db=db, user_id=user_id)
    if user_exists:
        return crud.create_user_skill(db=db, skill=skill, user_id=user_id)
    else:
        raise HTTPException(status_code=400, detail="User does not exist")

@router.post("/users/{user_name}/skills/", response_model=SkillPublic, tags=["skills"])
def create_skill_for_user_using_username_without_image(user_name: str, skill: SkillCreate, db: Session = Depends(get_db)):
    user_exists = crud.get_user_by_username(db=db, username=user_name)
    if user_exists:
        return crud.create_user_skill(db=db, skill=skill, user_id=user_exists.__dict__["id"])
    else:
        raise HTTPException(status_code=400, detail="User does not exist")

@router.post("/users/{user_name}/skills_image/", response_model=SkillPublic, tags=["skill", "upload"])
def create_skill_for_user_using_username_with_image(
    user_name: str,  skill: SkillCreate,  db: Session = Depends(get_db)
    ):

    print("------------------------------------------>Hello<------------------------------------------")
    user_exists = crud.get_user_by_username(db=db, username=user_name)
    # Check if user exits
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist")

    # Save image and create new file name
    # filename = image_file.filename
    # extention = filename.split(".")[1]
    # if extention not in {"png", "jpg"}:
        # raise HTTPException(status_code=406, detail="Not an png or jpg file")
    # generated_name_path = IMAGE_FILE_PATH + str(gen_unique_name()) + "." + extention
    # file_content = image_file.file.read()
    # with open(generated_name_path, "wb") as image:
        # image.write(file_content)
    # print(f"----------------------->{generated_name_path}")
    generated_name_path = str(gen_unique_name())

    return crud.create_user_skill(db=db, skill=skill, user_id=user_exists.__dict__["id"], cert_image_path=generated_name_path)

