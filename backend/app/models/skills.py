from typing import Optional

from app.models.core import CoreModel, IDModelMixin

class SkillBase(CoreModel):
    name: Optional[str]
    contact_info: Optional[str]
    test_data: Optional[int] = 0

class CreateSkill(SkillBase):
    name: str
    contact_info: str
    test_data: int

class UpdateSkill(SkillBase):
    contact_info: str
    test_data: int

class SkillInDB(IDModelMixin, SkillBase):
    name: str
    contact_info: str
    test_data: int

class SkillPublic(IDModelMixin, SkillBase):
    ...

