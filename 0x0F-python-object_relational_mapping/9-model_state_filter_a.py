#!/usr/bin/python3
"""
- A script that lists all State objects that contain the letter a
  from the database hbtn_0e_6_usa
- Your script should take 3 arguments: mysql username, mysql password
  and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
  port 3306
- Results must be sorted in ascending order by states.id
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
    query_result = session.query(State).filter(State.name.ilike('%a%')).\
        order_by(State.id).all()
    for result in query_result:
        print("{}: {}".format(result.id, result.name))
    session.close()
