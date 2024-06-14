"""Table classes for the database"""

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Level(Base):
  __tablename__ = "level"

  id = Column(Integer, primary_key=True, autoincrement=True)
  raw_name = Column(String)
  name = Column(String)


class Score(Base):
  __tablename__ = "game_data"

  id = Column(Integer, primary_key=True, autoincrement=True)
  timestamp = Column(Integer)  # unix timestamp
  era = Column(Integer)
  username1 = Column(String)
  username2 = Column(String)
  level_id = Column(Integer, ForeignKey("level.id"))
  score = Column(Integer)
  country = Column(String)
  platform = Column(String)
  mode = Column(Integer)

  level = relationship("Level")
