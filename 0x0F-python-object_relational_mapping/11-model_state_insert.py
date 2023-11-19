#!/usr/bin/python3
"""
- A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
- Your script should take 3 arguments: mysql username, mysql password and
  database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
  port 3306
- Print the new states.id after creation
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(db_user, db_passwd, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name = 'Louisiana')
    
    session.add(new_state)
    session.commit()

    query_result = session.query(State).filter(State.name == 'Louisiana')
    for result in query_result:
        print(result.id)

    session.close()
