from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from database.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(String)

    def __init__(self, name, state):
        self.name = name
        self.state = state