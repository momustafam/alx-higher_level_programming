#!/usr/bin/python3
'''
    A simple module since it has a one function.
'''
import MySQLdb
from sys import argv


def main():
    '''
        Lists all cities from the database hbtn_0e_4_usa.
    '''

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
