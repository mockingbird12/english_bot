import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData()
users_state = Table('users_state', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('state', Integer))
metadata.create_all(engine)



class User:

    def __init__(self, name, state):
        self.name = name
        self.state = state

mapper(User, users_state)

Session = sessionmaker(bind=engine)
session = Session()
user1 = User('user1', 'login')
session.add(user1)
ourUser = session.query(User).filter_by(name='user1').first()
print(ourUser)
