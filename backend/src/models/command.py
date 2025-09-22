from pydantic import BaseModel
from typing import Optional

class PlayerCommand(BaseModel):
    playerId: int
    command: str

class ProcessedCommand(BaseModel):
    playerId: int
    action: str
    target: Optional[str] = None
    metaData: Optional[dict] = None

