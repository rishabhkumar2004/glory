from app.db.repositories.base import BaseRepository
from app.models.skills import CreateStudent, StudentInDB, UpdateStudent 

CREATE_SKILLS_QUERY = """
    INSERT INTO students (name, college, year)
    VALUES (:name, :college, :year)
    RETURNING id, name, college, year
"""

GET_SKILL_BY_ID_QUERY = """
    SELECT id, name, college, year
    FROM students
    WHERE id = :id
"""

class StudentsRepository(BaseRepository):
    """
    All database actions associated with the Studenst resource
    """
    
    async def create_students(self, *, new_student: CreateStudent) -> StudentInDB:
        query_values = new_student.dict()
        student = await self.db.fetch_one(query=CREATE_SKILLS_QUERY, values=query_values)

        return StudentInDB(**student)

    async def get_student_info_by_id(self, *, id: int):
        student = await self.db.fetch_one(query=GET_SKILL_BY_ID_QUERY, values={"id": id})

        if not student:
            return None

        return StudentInDB(**student)

