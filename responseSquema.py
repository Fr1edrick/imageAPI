from pydantic import BaseModel

class ResponseSquema(BaseModel):
    filename    : str
    classes     : str
    predictions : str
    prediction  : str
    score       : str
