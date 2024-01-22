from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import Base
from .connection import engine
from .routers import users, skills
from . import config

def get_application():
    # Create all the tables
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(users.router)
    app.include_router(skills.router)

    return app


app = get_application()

