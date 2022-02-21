from datetime import datetime

from sqlalchemy.sql.sqltypes import Float
from app.configs.database import db
from sqlalchemy import Column, Integer, String,DateTime,Float
from dataclasses import dataclass


@dataclass
class SerieModel(db.Model):
   
    serie:str
    seasons:int
    released_date: datetime
    genre: str
    imdb_rating: float

    __tablename__ = "ka_series"
    id = Column(Integer, primary_key=True)
    serie = Column(String,unique=True,nullable=False)
    seasons = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    released_date = Column(DateTime)
    imdb_rating = Column(Float)
