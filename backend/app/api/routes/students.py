from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.models.students import CreateStudent, StudentInfoPublic
from app.db.repositories.students import StudentsRepository
from app.api.dependencies.database import get_repository


router = APIRouter()

@router.get("/")
async def get_student_info() -> List[dict]:
    skills = [
        {"id": 1, "name": "John Doe", "college": "ABESEC", "year": 1},
        {"id": 2, "name": "Mary Sue", "college": "ABESEC", "year": 2}
    ]

    return skills

@router.get("/{id}/", response_model=StudentInfoPublic, name="students:get-student-info-by-id")
async def get_student_info_by_id(
    id: int,
    sktudents_repo: StudentsRepository = Depends(get_repository(StudentsRepository))
    ) -> StudentInfoPublic:
    student = await sktudents_repo.get_student_info_by_id(id=id)
    if not student:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No student found with that id")

    return student

@router.post("/", response_model=StudentInfoPublic, name="students:create-student", status_code=HTTP_201_CREATED)
async def create_new_skill(
    new_student: CreateStudent = Body(..., embed=True),
    students_repo: StudentsRepository = Depends(get_repository(StudentsRepository))
    ) -> StudentInfoPublic:
    create_student = await students_repo.create_students(new_student=new_student)
    return create_student


