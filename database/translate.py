from sqlalchemy import Column, Integer, String
from database.base import Base

class Translate(Base):
    __tablename__ = 'translate'
    id = Column(Integer, primary_key=True)
    translate = Column(String)

    def __init__(self, translate):
        self.translate = translate