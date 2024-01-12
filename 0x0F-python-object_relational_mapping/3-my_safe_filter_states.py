#!/usr/bin/python3
'''
    A simple module since it has a one function main().
'''
import MySQLdb
from sys import argv


def main():
    '''
        Displays all values in the states table of hbtn_0e_0_usa where name
        matches the fourth given cmd argument.
    '''

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    key = argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("""
                SELECT *
                FROM states
                WHERE name LIKE BINARY %s
                ORDER BY id
                """, (key,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
