from sqlalchemy.orm import Session
from argon2 import PasswordHasher

from . import models
from schema import users, skills

hasher = PasswordHasher()

def create_user(*, db: Session, user: users.UserCreate):
    hashed_password = hasher.hash(user.password)
    db_user = models.Users(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh()
    return db_user

def get_user_by_username(*, db: Session, username: str):
    return db.query(models.Users).filter(username == models.Users.username).first()

def get_user_by_email(*, db: Session, email: str):
    return db.query(models.Users).filter(email == models.Users.email).first()

