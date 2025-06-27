#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa.
Results are sorted by cities.id in ascending order."""

import MySQLdb
import sys


def main():
    """Connects to MySQL and lists cities for the state given as argument."""
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cur.execute(query, (state_name,))

    cities = [city[0] for city in cur.fetchall()]

    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
