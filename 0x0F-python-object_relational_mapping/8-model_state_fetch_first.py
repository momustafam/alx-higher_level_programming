#!/usr/bin/python3
'''
     A simple module since it has a one function.
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def first_state(username, password, db_name):
    '''
        Prints the first `State` object from the databse hbtn_0e_0_usa.
    '''

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    first_state(argv[1], argv[2], argv[3])
