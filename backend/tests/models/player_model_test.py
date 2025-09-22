import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import Base
from src.models.player import PlayerORM


DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_player(setup_db):
    db = setup_db

    player = PlayerORM(
        name="TestPlayer",
        hp=120,
        xp=50,
        level=2,
        cluster="Alpha",
        inventory=[{"item": "Sword", "level": 3}]
    )
    db.add(player)
    db.commit()
    db.refresh(player)

    assert player.player_id is not None
    assert player.name == "TestPlayer"
    assert player.hp == 120
    assert player.level == 2
    assert player.inventory[0]["item"] == "Sword"
    assert player.inventory[0]["level"] == 3


def test_update_inventory(setup_db):
    db = setup_db
    # Get the first player
    player = db.query(PlayerORM).first()
    # Add new item to inventory
    player.inventory.append({"item": "Shield", "level": 1})
    db.commit()
    db.refresh(player)

    assert len(player.inventory) == 2
    assert player.inventory[1]["item"] == "Shield"
    assert player.inventory[1]["level"] == 1
