#!/usr/bin/python3
"""Safely displays all values in the states table where name matches
the argument from the database hbtn_0e_0_usa. Prevents SQL injection.
Results are sorted by id."""

import MySQLdb
import sys


def main():
    """Connects securely to MySQL and retrieves states that match a
    user-given name, using parameterized queries to prevent SQL injection."""
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
