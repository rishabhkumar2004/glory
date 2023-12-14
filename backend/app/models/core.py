from pydantic import BaseModel

class CoreModel(BaseModel):
    """
    All common logic for other classes goes here
    """
    pass

class IDModelMixin(BaseModel):
    id: int
