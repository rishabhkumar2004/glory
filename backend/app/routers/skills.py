from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schema import skills
from ..dependencies import get_db
from .. import crud

router = APIRouter()

@router.post("/users/{user_id}/skills/", response_model=skills.SkillPublic, tags=["skills"])
def create_skill_for_user(user_id: int, skill: skills.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_user_skill(db=db, skill=skill, user_id=user_id)

