from app.db.repositories.base import BaseRepository
from app.models.cleanings import CleaningCreate, CleaningInDB, CleaningUpdate 

CREATE_SKILLS_QUERY = """
    INSERT INTO skills (name, description, price, cleanings_type)
    VALUES (:name, :description, :price, :cleanings_type)
    RETURNING id, name, description, price, cleanings_type
"""

class CleaningsRepository(BaseRepository):
    """
    All database actions associated with the Cleanings resource
    """
    
    async def create_cleanings(self, *, new_cleaning: CleaningCreate) -> CleaningInDB:
        query_values = new_cleaning.dict()
        cleaning = await self.db.fetch_one(query=CREATE_SKILLS_QUERY, values=query_values)

        return CleaningInDB(**cleaning)

