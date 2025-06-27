#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects to DB and deletes all State objects with 'a' in the name."""
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
