from database.user import User
from database.words import Word
from database.translate import Translate
from database.base import Base, engine, Session

Base.metadat.create_all(engine)

def insert_user(username, state):
    session = Session()
    user = User(username, state)
    session.add(user)
    session.commit()
    session.close()

def insert_word(eng_word):
    session = Session()
    word = Word(eng_word)
    session.add(word)
    session.commit()
    session.close()

def insert_translate(translate_word):
    session = Session()
    translate = Translate(translate_word)
    session.add(translate)
    session.commit()
    session.close()