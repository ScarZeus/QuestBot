from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base



class DragonORM(Base):
    __tablename__ = "dragons"

    id = Column(Integer, primary_key=True, index=True)
    fire_power = Column(Integer, nullable=False)
    move_speed = Column(Integer, nullable=False)
    hp = Column(Integer, default=1000)

    moves = relationship("MoveORM", back_populates="dragon", cascade="all, delete-orphan")


class MoveORM(Base):
    __tablename__ = "moves"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    damage = Column(Integer, nullable=False)

    dragon_id = Column(Integer, ForeignKey("dragons.id"))
    dragon = relationship("DragonORM", back_populates="moves")



class Move(BaseModel):
    name: str
    damage: int


class Dragon(BaseModel):
    fire_power: int
    move_speed: int
    hp: int = 1000
    moves: List[Move] = []

    def __init__(self, fire_power: int, move_speed: int, hp: int = 1000, moves: Optional[List[Move]] = None):
        super().__init__(fire_power=fire_power, move_speed=move_speed, hp=hp, moves=moves or [])
