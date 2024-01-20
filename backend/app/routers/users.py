from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schema import skills, users
from ..dependencies import get_db
from .. import crud

router = APIRouter()

@router.post("/users/", response_model=users.UserPublic, tags=["users"])
def create_user(user: users.UserCreate, db: Session = Depends(get_db)):
    email_in_use = crud.get_user_by_email(db=db, email=user.email)
    username_in_use = crud.get_user_by_username(db=db, username=user.username)
    if email_in_use:
        raise HTTPException(status_code=400, detail="Email is already in use")
    if username_in_use:
        raise HTTPException(status_code=400, detail="Username is already in use")
    return crud.create_user(db=db, user=user)

