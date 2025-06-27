#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument
from the database hbtn_0e_0_usa. Results are sorted by states.id ascending."""

import MySQLdb
import sys


def main():
    """Connects to MySQL and fetches states matching the given name."""
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC", (sys.argv[4],)
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
