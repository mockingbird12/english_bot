from sqlalchemy import Column, Integer, String, Table, ForeignKey
from database.base import Base


words_translate_association = Table(
    'words_translation', Base.metadata,
    Column('words_id', Integer, ForeignKey('words.id')),
    Column('translate_id', Integer, ForeignKey('translate.id'))
)


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String)

    def __init__(self, word):
        self.word = word