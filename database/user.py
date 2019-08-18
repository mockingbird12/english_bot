from sqlalchemy import Column, Integer, String
from database.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    state = Column(String)

    def __init__(self, name, state):
        self.name = name
        self.state = state