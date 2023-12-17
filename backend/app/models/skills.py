from typing import Optional

from app.models.core import CoreModel, IDModelMixin

class StudentInfoBase(CoreModel):
    name: Optional[str]
    college: Optional[str]
    year: Optional[int] = 1

class CreateStudent(StudentInfoBase):
    name: str
    college: str
    year: int

class UpdateStudent(StudentInfoBase):
    college: str
    year: int

class StudentInDB(IDModelMixin, StudentInfoBase):
    name: str
    college: str
    year: int

class StudentInfoPublic(IDModelMixin, StudentInfoBase):
    ...

