#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database
hbtn_0e_0_usa, sorted by states.id in ascending order."""

import MySQLdb
import sys


def main():
    """Connects to MySQL and displays all states starting with 'N'."""
    username, password, db_name = sys.argv[1:4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
