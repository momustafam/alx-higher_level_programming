#!/usr/bin/python3
'''
    A simple Module since it has a one function main().
'''
import MySQLdb
from sys import argv


def main():
    '''
        Function that lists all states from the database hbtn_0e_0_usa.
    '''
    my_user, my_pass, my_db = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=my_user,
                         passwd=my_pass, db=my_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
