from os import name
import sqlite3

CREATE_FOOD_TABLE = "CREATE TABLE IF NOT EXISTS foodtable (id INTEGER PRIMARY KEY, name TEXT , category TEXT," \
                    "rating INTEGER); "
INSERT_FOOD = "INSERT INTO foodtable(name, category , rating) VALUES (?, ?, ?);"
GET_ALL_FOODS = "SELECT * FROM foodtable;"
GET_FOODS_BY_NAME = "SELECT * FROM foodtable WHERE name = ?; "
GET_THE_BEST_FOOD = """
SELECT * FROM foodtable 
WHERE name = ?
ORDER BY rating DESC
LIMIT 1
 """


def connect():
    return sqlite3.connect("test_db1.db")


def create_tables(conn):
    with conn:
        conn.execute(CREATE_FOOD_TABLE)


def add_food(conn, name, category, rating):
    with conn:
        conn.execute(INSERT_FOOD, (name, category, rating))


def get_all_foods(conn,):
    with conn:
        return conn.execute(GET_ALL_FOODS,).fetchall()


def get_foods_by_name(conn,name):
    with conn:
        return conn.execute(GET_FOODS_BY_NAME,(name,)).fetchall()


def get_best_category_by_name(conn, name):
    with conn:
        return conn.execute(GET_THE_BEST_FOOD,(name,)).fetchone()
