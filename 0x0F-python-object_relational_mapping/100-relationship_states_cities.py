#!/usr/bin/python3
"""
- A script that creates the State “California” with the City
  “San Francisco” from the database hbtn_0e_100_usa
- Your script should take 3 arguments: mysql username, mysql password and
  database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on localhost at
  port 3306
- You must use the cities relationship for all State objects
- Your code should not be executed when imported
"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_city)
    session.commit()
