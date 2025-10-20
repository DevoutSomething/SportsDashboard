#file containing code to create db
import psycopg2
import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

try:
    connection = psycopg2.connect(
        host=os.getenv("HOST"),
        dbname=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        sslmode=os.getenv("SSLMODE"))
    print("Connection successful!")

    cur = connection.cursor()

    #create tables
    cur.execute("""
    CREATE TABLE IF NOT EXISTS team (
        tid SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        conference VARCHAR(50),
        division VARCHAR(50)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS player (
        pid SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        position VARCHAR(20),
        birth_date DATE,
        height INT,
        weight INT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game (
        gid SERIAL PRIMARY KEY,
        home_team INT REFERENCES team(tid) ON DELETE RESTRICT ON UPDATE CASCADE,
        away_team INT REFERENCES team(tid) ON DELETE RESTRICT ON UPDATE CASCADE,
        date DATE,
        season VARCHAR(20),
        home_score INT,
        away_score INT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_stats (
        gid INT REFERENCES game(gid),
        pid INT REFERENCES player(pid),
        tid INT REFERENCES team(tid),
        minutes INT CHECK(minutes >= 0),
        pts INT,
        off_rebound INT,
        def_rebound INT,
        assists INT,
        steals INT,
        blocks INT,
        fgm INT,
        fga INT CHECK(fga >=fgm),
        3pm INT,
        3pa INT CHECK(3pa >= 3pm),
        ftm INT,
        fta INT CHECK(fta >=ftm),
        turnovers INT,
        fouls INT,
        PRIMARY KEY (gid, pid)
    );
    """)

    #commit table creation
    connection.commit()

    #create triggers

    #adding/editing game stats

    #Create views for queries

except:
    print("Failed to connect")

if connection:
    connection.close()
    print("Connection closed")