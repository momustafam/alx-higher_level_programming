#!/usr/bin/python3
'''
    A simple module since it has one function called `print_cities`.
'''

from sys import argv
from model_state import State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(City, State).filter(City.state_id == State.id) \
        .order_by(City.id)

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
