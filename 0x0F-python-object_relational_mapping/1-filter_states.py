#!/usr/bin/python3
"""
A script that lists all states with a name starting with N from the database
hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=db_user, passwd=db_passwd,
                         db=db_name, charset='utf8')
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%'
                ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
