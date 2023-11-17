#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
- Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost
at port 3306
- Results must be sorted in ascending order by states.id
- Your code should not be executed when imported
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
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (argument,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
