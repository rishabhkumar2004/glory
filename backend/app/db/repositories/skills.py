from app.db.repositories.base import BaseRepository
from app.models.skills import CreateSkill, SkillInDB, UpdateSkill 

CREATE_SKILLS_QUERY = """
    INSERT INTO skills (name, contact_info, test_data)
    VALUES (:name, :contact_info, :test_data)
    RETURNING id, name, contact_info, test_data
"""

class SkillsRepository(BaseRepository):
    """
    All database actions associated with the Cleanings resource
    """
    
    async def create_skills(self, *, new_skill: CreateSkill) -> SkillInDB:
        query_values = new_skill.dict()
        skill = await self.db.fetch_one(query=CREATE_SKILLS_QUERY, values=query_values)

        return SkillInDB(**skill)

