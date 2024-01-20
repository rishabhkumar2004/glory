from pydantic import BaseModel

class SkillBase(BaseModel):
    title: str
    description: str

class SkillCreate(SkillBase):
    ...

class SkillPublic(SkillBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True


