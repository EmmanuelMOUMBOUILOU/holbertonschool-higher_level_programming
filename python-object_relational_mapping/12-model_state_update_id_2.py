#!/usr/bin/python3
"""Updates the name of the State object with id=2 to 'New Mexico'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Updates State.id=2 to have the name 'New Mexico'."""
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    main()
