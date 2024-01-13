#!/usr/bin/python3
'''
    A simple module since it has a one function (get_state).
'''
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state(user, pas, db, st):
    '''
        Prints the `State` object with the name passed as an argument
        from the database hbtn_0e_0_usa.
    '''

    engine = create_engine(
        f"mysql+mysqldb://{user}:{pas}@localhost:3306/{db}"
        )
    Session = sessionmaker(engine)

    with Session() as session:
        state = session.query(State).filter(State.name.like(st)).first()

    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    get_state(argv[1], argv[2], argv[3], argv[4])
