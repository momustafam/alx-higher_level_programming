#!/usr/bin/python3
'''
    A simple module since it has a one function (delete_state_a).
'''

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_state_a(user, pas, db):
    '''
        Deletes all `State` objects with a name containing the letter
        `a` from a database.
    '''

    engine = create_engine(
            f"mysql+mysqldb://{user}:{pas}@localhost:3306/{db}"
            )
    Session = sessionmaker(engine)
    session = Session()

    states_to_del = session.query(State).filter(State.name.like("%a%")).all()

    for state in states_to_del:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    delete_state_a(argv[1], argv[2], argv[3])
