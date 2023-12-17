from app.db.repositories.base import BaseRepository
from app.models.skills import CreateSkill, SkillInDB, UpdateSkill 

CREATE_SKILLS_QUERY = """
    INSERT INTO skills (name, contact_info, test_data)
    VALUES (:name, :contact_info, :test_data)
    RETURNING id, name, contact_info, test_data
"""

GET_SKILL_BY_ID_QUERY = """
    SELECT id, name, contact_info, test_data
    FROM skills
    WHERE id = :id
"""

class SkillsRepository(BaseRepository):
    """
    All database actions associated with the Cleanings resource
    """
    
    async def create_skills(self, *, new_skill: CreateSkill) -> SkillInDB:
        query_values = new_skill.dict()
        skill = await self.db.fetch_one(query=CREATE_SKILLS_QUERY, values=query_values)

        return SkillInDB(**skill)

    async def get_skill_by_id(self, *, id: int):
        skill = await self.db.fetch_one(query=GET_SKILL_BY_ID_QUERY, values={"id": id})

        if not skill:
            return None

        return SkillInDB(**skill)

