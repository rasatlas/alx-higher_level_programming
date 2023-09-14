# 0x0F. Python - Object-relational mapping
`Python` `OOP` `SQL` `MySQL` `ORM` `SQLAlchemy`

## Background Context
In this project, we will link two amazing worlds: Databases and Python!<br>

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute our SQL queries.<br>

In the second part, we will use the module SQLAlchemy, an Object Relational Mapper (ORM).<br>

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, our biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. We won’t write any SQL queries only Python code. Last thing, our code won’t be “storage type” dependent. We will be able to change our storage easily without re-writing our entire project.<br>

__Without ORM:__


```sql
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```


__With an ORM:__


```sql
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```


## Learning Objectives
### General
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy

## More Info
__Install and activate venv__
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```


__Install `MySQLdb` module version `2.0.x`__
For installing MySQLdb, you need to have MySQL installed.


```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```


__Install `SQLAlchemy` module version `1.4.x`__


```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:

```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```
You can ignore it.

## Tasks

0. Write a script that lists all states from the database hbtn_0e_0_usa:
    - Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported

1. Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
    - Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported

2. Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
    - Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - You must use format to create the SQL query with the user input
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported

3. Write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
    - Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported

4. Write a script that lists all cities from the database hbtn_0e_4_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported

5. Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
    - Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
    - The results must be displayed as they are in the example below
    - Your code should not be executed when imported

6. Write a python file that contains the class definition of a State and an instance Base = declarative_base():
    - State class:
        - inherits from Base Tips
        - links to the MySQL table states
        - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
        - class attribute name that represents a column of a string with maximum 128 characters and can’t be null
    - You must use the module SQLAlchemy
    - Your script should connect to a MySQL server running on localhost at port 3306
    - WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

7. Write a script that lists all State objects from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - The results must be displayed as they are in the example below
    - Your code should not be executed when imported

8. Write a script that prints the first State object from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - The state you display must be the first in states.id
    - You are not allowed to fetch all states from the database before displaying the result
    - The results must be displayed as they are in the example below
    - If the table states is empty, print Nothing followed by a new line
    - Your code should not be executed when imported

9. Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - The results must be displayed as they are in the example below
    - Your code should not be executed when imported

10. Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
    - Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display Not found
    - Your code should not be executed when imported

11. Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Print the new states.id after creation
    - Your code should not be executed when imported

12. Write a script that changes the name of a State object from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Change the name of the State where id = 2 to New Mexico
    - Your code should not be executed when imported

13. Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Your code should not be executed when imported

14. Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
    - City class:
        - inherits from Base (imported from model_state)
        - links to the MySQL table cities
        - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
        - class attribute name that represents a column of a string of 128 characters and can’t be null
        - class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
    - You must use the module SQLAlchemy<br>

Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
    - Your code should not be executed when imported

15. Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:
    - City class:
        - No change
    - State class:
        - In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
    - You must use the module SQLAlchemy<br>

Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - Your script should connect to a MySQL server running on localhost at port 3306
    - You must use the cities relationship for all State objects
    - Your code should not be executed when imported

16. Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - The connection to your MySQL server must be to localhost on port 3306
    - You must only use one query to the database
    - You must use the cities relationship for all State objects
    - Results must be sorted in ascending order by states.id and cities.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported

17. Write a script that lists all City objects from the database hbtn_0e_101_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - Your script should connect to a MySQL server running on localhost at port 3306
    - You must use only one query to the database
    - You must use the state relationship to access to the State object linked to the City object
    - Results must be sorted in ascending order by cities.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported