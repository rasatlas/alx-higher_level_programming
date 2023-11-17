#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    argument = sys.argv[4]
    db_host = 'localhost'
    db_port = 3306

    db = MySQLdb.connect(host=db_host, port=db_port, user=db_user,
                         passwd=db_passwd, db=db_name, charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE {} = '{}'\
                ORDER BY id ASC".format('name', argument))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
