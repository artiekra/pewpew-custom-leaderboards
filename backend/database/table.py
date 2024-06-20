"""Table classes for the database"""

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

# [TODO: reconsider using _timestamp, _level_, _mode]
# [TODO: add additional validation]
class ScoreBase(SQLModel):
    """Base class to represent scores"""

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
    """Class to represent scores in the database (with auto-increment
    primary-key id"""
    id: int | None = Field(default=None, primary_key=True)


class ScoreCreate(ScoreBase):
    """Class to represent scores (when creating/inserting one with api"""
    pass


class ApiRequest(SQLModel, table=True):
    """Class to represent API request (for logging into database)"""

    id: int | None = Field(default=None, primary_key=True)
    method: str
    path: str
    ip: str | None = None  # seems to always be available.. privacy tho?
    json_body: str | None = None
