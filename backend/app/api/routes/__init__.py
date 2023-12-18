from fastapi import APIRouter

from app.api.routes.students import router as skills_router


router = APIRouter()

router.include_router(skills_router, prefix="/skills", tags=["skills"])
