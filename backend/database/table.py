"""Table classes for the database"""

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


# [TODO: reconsider using _timestamp, _level_, _mode]
# [TODO: add additional validation]
class ScoreBase(SQLModel):
    timestamp: int
    era: int
    username1: str
    username2: str | None = None
    level: str 
    score: int
    country: str | None = None
    platform: str | None = None
    mode: int


class Score(ScoreBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ScoreCreate(ScoreBase):
    pass
