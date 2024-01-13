#!/usr/bin/python3
'''
    A simple module since it lists all `State` objects, and corresponding
    `City` objects, contained in the database "hbtn_0e_0_usa".
'''

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
