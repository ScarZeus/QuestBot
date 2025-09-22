from pydantic import BaseModel
from typing import Optional, List, Dict
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from app.db.database import Base

class PlayerORM(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    hp = Column(Integer, default=100)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    cluster = Column(String, nullable=True)
    inventory = Column(JSON, default=[])


class InventoryItem(BaseModel):
    item: str
    level: int = 1

class Player(BaseModel):
    player_id: int
    name: str
    hp: int = 100
    xp: int = 0
    level: int = 1
    cluster: Optional[str] = None
    inventory: Optional[List[InventoryItem]] = []
