#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
- Your script should take 4 arguments: mysql username, mysql password,
  database name and state name (SQL injection free!)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at
  port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- Your code should not be executed when imported
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    arg_state = sys.argv[4]
    db_host = 'localhost'
    db_port = 3306

    db = MySQLdb.connect(host=db_host, port=db_port,
                         user=db_user, passwd=db_passwd,
                         db=db_name, charset='utf8')
    cur = db.cursor()
    query = """
                SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE BINARY states.name = %s
                ORDER BY cities.id ASC
            """
    cur.execute(query, (arg_state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0], end='')
        if row != query_rows[-1]:
            print(end=', ')
    print()
    cur.close()
    db.close()
