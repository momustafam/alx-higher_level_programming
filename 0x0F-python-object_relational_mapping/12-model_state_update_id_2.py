#!/usr/bin/python3
'''
    A simple module since it has a one function (update_state).
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state(user, pas, db, st_id=2):
    '''
        Changes the name of a `State` object from the database hbtn_0e_0_usa.
    '''

    engine = create_engine(
            f"mysql+mysqldb://{user}:{pas}@localhost:3306/{db}"
            )
    Session = sessionmaker(engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()
    state_to_update.name = "New Mexico"

    session.commit()
    session.close()


if __name__ == "__main__":
    update_state(argv[1], argv[2], argv[3])
