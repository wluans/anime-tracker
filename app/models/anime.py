from pydantic import BaseModel
from typing import List

class Anime(BaseModel):
    id: int
    title: str
    episodes: int
    status: str
    genres: List[str]
    studio: str
    synopsis: str
    episodes_duration: int
