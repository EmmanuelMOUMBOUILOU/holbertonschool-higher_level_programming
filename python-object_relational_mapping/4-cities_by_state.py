#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa.
Results are sorted by cities.id in ascending order."""

import MySQLdb
import sys


def main():
    """Connects to the MySQL database and lists
      cities with their state names."""
    username, password, db_name = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    cur.execute(query)

    for city_id, city_name, state_name in cur.fetchall():
        print((city_id, city_name, state_name))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
