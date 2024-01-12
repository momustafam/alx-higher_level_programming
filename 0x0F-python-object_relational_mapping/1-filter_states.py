#!/usr/bin/python3
'''
    A simple module since it has a one function main().
'''
import MySQLdb
from sys import argv


def main():
    '''
        A function that lists all states with a name starting with `N`
        from the database hbtn_0e_0_usa.
    '''
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute('''
                SELECT *
                FROM states
                WHERE name LIKE "N%"
                ''')
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
