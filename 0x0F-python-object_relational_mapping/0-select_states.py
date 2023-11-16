#!/usr/bin/env python3

if __name__ == "__main__":
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306,
            user='root', password='root', db='hbtn_0e_0_usa', charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY ID ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
