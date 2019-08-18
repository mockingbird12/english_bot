from database.user import User
from database.words import Word
from database.translate import Translate
from database.base import Base, engine, Session

Base.metadata.create_all(engine)

def insert_user(username, state):
    session = Session()
    user = User(username, state)
    res = session.query(User).filter(User.name == username).all()
    if len(res) < 1:
        session.add(user)
        session.commit()
        session.close()
    else:
        print('User already exists')

def update_status(username, state):
    session = Session()
    res = session.query(User).filter(User.name == username).all()
    if len(res) < 1:
        user = User(username, state)
        session.add(user)
        session.commit()
        session.close()
    if len(res) == 1:
        user = session.query(User).filter(User.name == username).first()
        user.state = state
        session.commit()
        session.close()

def get_user_status(username):
    session = Session()
    user_info = session.query(User).filter(User.name == username).all()
    if user_info != []:
        return user_info[0].state
    else:
        return None

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