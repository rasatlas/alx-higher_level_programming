 #!/usr/bin/python3
  2 """
  3 A script that lists all states from the database hbtn_0e_0_usa:
  4
  5 Your script should take 3 arguments:
  6     mysql username, mysql password and database name
  7     (no argument validation needed)
  8 You must use the module MySQLdb (import MySQLdb)
  9 Your script should connect to a MySQL server running on localhost at port 3306
 10 Results must be sorted in ascending order by states.id
 11 Results must be displayed as they are in the example below
 12 Your code should not be executed when imported
 13 """
 14 import sys
 15 import MySQLdb
 16
 17 if __name__ == '__main__':
 18     db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
 19                          db=sys.argv[3], port=3306)
 20
 21     cur = db.cursor()
 22     cur.execute("SELECT * FROM states;")
 23     states = cur.fetchall()
 24
 25     for state in states:
 26         print(state)
