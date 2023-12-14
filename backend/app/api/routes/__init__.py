from fastapi import APIRouter

from app.api.routes.skills import router as skills_router


router = APIRouter()

router.include_router(skills_router, prefix="/skills", tags=["skills"])
