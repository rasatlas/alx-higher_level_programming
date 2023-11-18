#!/usr/bin/python3
"""
- A script that prints the first State object from the database hbtn_0e_6_usa
- Your script should take 3 arguments: mysql username, mysql password and
  database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state
  import Base, State
- Your script should connect to a MySQL server running on localhost at
  port 3306
- The state you display must be the first in states.id
- You are not allowed to fetch all states from the database before displaying
  the result
- If the table states is empty, print Nothing followed by a new line
- Your code should not be executed when imported
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session_var = session.query(State).order_by(State.id).first()
    if (session_var):
        print("{}: {}".format(session_var.id, session_var.name))
    else:
        print('Nothing')
    session.close()
