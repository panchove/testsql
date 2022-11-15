DROP TABLE IF EXISTS persons_hobbies;
DROP TABLE IF EXISTS persons_trades;
DROP TABLE IF EXISTS persons;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS states;
DROP TABLE IF EXISTS hobbies;
DROP TABLE IF EXISTS trades;

CREATE TABLE IF NOT EXISTS countries
(
	id INTEGER,
	name VARCHAR(100)NOT NULL,
	CONSTRAINT pk_countries PRIMARY KEY (id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS states
(
	id INTEGER,
	name VARCHAR(100)NOT NULL,
	CONSTRAINT pk_states PRIMARY KEY (id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS hobbies
(
	id INTEGER,
	name VARCHAR(100) NOT NULL,
	CONSTRAINT pk_hobbies PRIMARY KEY (id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS trades
(
	id INTEGER,
	name VARCHAR(100) NOT NULL,
	CONSTRAINT pk_trades PRIMARY KEY (id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS persons
(
	id INTEGER,
	fname VARCHAR(100) NOT NULL,
	lname VARCHAR(100) NOT NULL,
	dob DATE NOT NULL,
	salary float DEFAULT 0 CHECK (salary >= 0),
	state_id INTEGER NOT NULL,
	phone_code INTEGER NOT NULL,
	phone_number INTEGER NOT NULL,
	CONSTRAINT fk_persons_states FOREIGN KEY (state_id) REFERENCES states(id)
    	ON DELETE CASCADE
    	ON UPDATE CASCADE
	,
    CONSTRAINT pk_persons PRIMARY KEY (id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS persons_hobbies
(
	id INTEGER,
	person_id INTEGER NOT NULL,
	hobby_id INTEGER NOT NULL,
	CONSTRAINT fk_persons_person FOREIGN KEY (person_id) REFERENCES persons(id)
    	ON DELETE CASCADE
      	ON UPDATE CASCADE
	,
	CONSTRAINT fk_persons_hobby FOREIGN KEY (hobby_id) REFERENCES hobbies(id)
    	ON DELETE CASCADE
      	ON UPDATE CASCADE
	,	
	CONSTRAINT pk_persons_hobbies PRIMARY KEY (id AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS persons_trades
(
	id INTEGER,
	person_id INTEGER NOT NULL,
	trade_id INTEGER NOT NULL,
	CONSTRAINT fk_persons_person FOREIGN KEY (person_id) REFERENCES persons(id)
    	ON DELETE CASCADE
      	ON UPDATE CASCADE	
	,
	CONSTRAINT fk_persons_trade FOREIGN KEY (trade_id) REFERENCES trades(id)
    	ON DELETE CASCADE
      	ON UPDATE CASCADE
    ,
	CONSTRAINT pk_persons_trades PRIMARY KEY (id AUTOINCREMENT)
);
