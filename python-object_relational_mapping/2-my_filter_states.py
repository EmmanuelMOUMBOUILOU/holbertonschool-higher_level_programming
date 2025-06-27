#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument
from the database hbtn_0e_0_usa. Results are sorted by states.id ascending."""

import MySQLdb
import sys


def main():
    """Connects to a MySQL database and retrieves states
      that match a given name,
    ensuring results are sorted by id in ascending order."""
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    safe_name = state_name.replace("'", "''")

    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(safe_name)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
