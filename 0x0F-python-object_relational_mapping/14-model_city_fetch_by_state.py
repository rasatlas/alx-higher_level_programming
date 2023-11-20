#!/usr/bin/python3
"""
- A script that prints all City objects from the database hbtn_0e_14_usa
- Your script should take 3 arguments: mysql username, mysql password and
  database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at
  port 3306
- Results must be sorted in ascending order by cities.id
- Results must be display as (<state name>: (<city id>) <city name>)
- Your code should not be executed when imported
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(City, State.id == City.state_id).\
        order_by(City.id).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
