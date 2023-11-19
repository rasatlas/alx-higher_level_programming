#!/usr/bin/python3
"""
- A script that prints the State object with the name passed as argument
  from the database hbtn_0e_6_usa
- Your script should take 4 arguments: mysql username, mysql password,
  database name and state name to search (SQL injection free)
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
  port 3306
- You can assume you have one record with the state name to search
- Results must display the states.id
- If no state has the name you searched for, display Not found
- Your code should not be executed when imported
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    arg_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(db_user, db_passwd, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_result = session.query(State).\
            filter(State.name.ilike(arg_name)).all()
    if (query_result):
        for result in query_result:
            print(result.id)
    else:
        print("Not found")
    session.close()
