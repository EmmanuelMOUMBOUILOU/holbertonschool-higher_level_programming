#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main():

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
