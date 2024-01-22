from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema.skills import SkillCreate, SkillPublic
from app.dependencies import get_db
from app import crud

router = APIRouter()

@router.post("/users/{user_id}/skills/", response_model=SkillPublic, tags=["skills"])
def create_skill_for_user_using_id(user_id: int, skill: SkillCreate, db: Session = Depends(get_db)):
    user_exists = crud.get_user_by_id(db=db, user_id=user_id)
    if user_exists:
        return crud.create_user_skill(db=db, skill=skill, user_id=user_id)
    else:
        raise HTTPException(status_code=400, detail="User does not exist")

@router.post("/users/{user_name}/skills/", response_model=SkillPublic, tags=["skills"])
def create_skill_for_user_using_username(user_name: str, skill: SkillCreate, db: Session = Depends(get_db)):
    user_exists = crud.get_user_by_username(db=db, username=user_name)
    if user_exists:
        return crud.create_user_skill(db=db, skill=skill, user_id=user_exists.__dict__["id"])
    else:
        raise HTTPException(status_code=400, detail="User does not exist")

