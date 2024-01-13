#!/usr/bin/python3
'''
    A simple module since it has a one function add_state.
'''

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state(user, pas, db):
    '''
        Adds the `State` object "Louisiana" to the database hbtn_0e_0_usa.
    '''

    engine = create_engine(
            f"mysql+mysqldb://{user}:{pas}@localhost:3306/{db}"
            )
    Session = sessionmaker(engine)
    louisiana = State(name="Louisiana")
    session = Session()
    session.add(louisiana)
    session.commit()

    print(louisiana.id)
    session.close()

if __name__ == "__main__":
    add_state(argv[1], argv[2], argv[3])
