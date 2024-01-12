#!/usr/bin/python3
'''
    A simple module since it has a one function.
'''
import MySQLdb
from sys import argv


def main():
    '''
        Lists all cities of a given state using the database hbtn_0e_4_usa.
    '''

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""
                SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id
                """, (argv[4],))

    rows = cur.fetchall()
    for i in range(len(rows) - 1):
        print(rows[i][0], end=", ")
    print(rows[i+1][0])

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
