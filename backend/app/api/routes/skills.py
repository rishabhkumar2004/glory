from typing import List

from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from app.models.skills import CreateSkill, SkillPublic
from app.db.repositories.skills import SkillsRepository
from app.api.dependencies.database import get_repository


router = APIRouter()

@router.get("/")
async def get_all_skills() -> List[dict]:
    skills = [
        {"id": 1, "name": "John Doe", "contact_info": "john.doe@example.com", "test_data": 50},
        {"id": 2, "name": "Mary Sue", "contact_info": "mary.sue@example.com", "test_data": 100}
    ]

    return skills

@router.post("/", response_model=SkillPublic, name="cleanings:create-cleaning", status_code=HTTP_201_CREATED)
async def create_new_skill(
    new_cleaning: CreateSkill = Body(..., embed=True),
    cleanings_repo: SkillsRepository = Depends(get_repository(SkillsRepository))
    ) -> SkillPublic:
    create_cleaning = await cleanings_repo.create_cleanings(new_cleaning=new_cleaning)
    return create_cleaning


