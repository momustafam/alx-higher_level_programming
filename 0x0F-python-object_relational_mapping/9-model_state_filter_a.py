#!/usr/bin/python3
'''
    A simple model since it has a one function (filter_state)
'''
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_state(user, pas, db):
    '''
        Lists all `State` objects that contain the letter a from
        the database hbtn_0e_0_usa
    '''

    engine = create_engine(
        f"mysql+mysqldb://{user}:{pas}@localhost:3306/{db}"
        )
    Session = sessionmaker(engine)

    with Session() as session:
        states = session.query(State).filter(State.name.like("%a%"))
        states = states.order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    filter_state(argv[1], argv[2], argv[3])
