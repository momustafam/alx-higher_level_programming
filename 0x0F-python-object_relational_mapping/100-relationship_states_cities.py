#!/usr/bin/python3
'''
    A simple module since it has a one function called `create_state`.
'''

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_state(usr, pas, db):
    '''Creates the `State` California` with the `City` "San Francisco.'''

    db_url = f"mysql+mysqldb://{usr}:{pas}@localhost:3306/{db}"
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    san_francisco = State(name="California",
                          cities=[City(name="San Francsico")])

    session.add(san_francisco)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_state(argv[1], argv[2], argv[3])
