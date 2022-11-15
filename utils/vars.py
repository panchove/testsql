SQL_INSERT_COUNTRY="""
INSERT INTO countries(name) VALUES(?);
"""

SQL_INSERT_STATE="""
INSERT INTO states(name) VALUES(?);
"""

SQL_INSERT_HOBBY="""
INSERT INTO hobbies(name) VALUES(?);
"""

SQL_INSERT_TRADE="""
INSERT INTO trades(name) VALUES(?);
"""

SQL_INSERT_PERSON="""
INSERT INTO 
	persons(fname, lname, dob, salary, state_id, phone_code, phone_number) 
VALUES(?, ?, ?, ?, ?, ?, ?);
"""
