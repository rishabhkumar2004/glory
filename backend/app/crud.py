from operator import mod
from sqlalchemy.orm import Session
from argon2 import PasswordHasher

from . import models
from .schema import users, skills

hasher = PasswordHasher()

def create_user(*, db: Session, user: users.UserCreate):
    hashed_password = hasher.hash(user.password)
    db_user = models.Users(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_skill(*, db: Session, skill: skills.SkillCreate, user_id: int):
    db_skill = models.Skills(**skill.model_dump(), user_id=user_id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def get_user_by_username(*, db: Session, username: str):
    return db.query(models.Users).filter(username == models.Users.username).first()

def get_user_by_email(*, db: Session, email: str):
    return db.query(models.Users).filter(email == models.Users.email).first()

