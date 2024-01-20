from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users, skills
from . import config

def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(users.router)

    return app


app = get_application()
