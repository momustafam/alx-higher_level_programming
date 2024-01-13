#!/usr/bin/python3
'''
    A simple module since it lists all `City` objects from the given DB.
'''

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(engine)
    session = Session()

    cities = session.query(City).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
