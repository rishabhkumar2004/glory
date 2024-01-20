from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .connection import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    skills = relationship("Skills", back_populates="user")

class Skills(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, index=True)
    description = Column(String, default=None)

    user = relationship("Users", back_populates="skills")

