#!/usr/bin/python3
"""Prints the State.id of a State object with a given name from the DB."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Searches for a state by name and prints its id, or 'Not found'."""
    username, password, db_name, state_name = sys.argv[1:5]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
