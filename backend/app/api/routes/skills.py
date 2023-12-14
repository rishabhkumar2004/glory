from typing import List

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_skills() -> List[dict]:
    skills = [
        {"id": 1, "name": "John Doe", "contact_info": "john.doe@example.com", "test_data": 50},
        {"id": 2, "name": "Mary Sue", "contact_info": "mary.sue@example.com", "test_data": 100}
    ]

    return skills

