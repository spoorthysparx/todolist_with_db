import sqlite3

def db_connection(sql_query):
     with sqlite3.connect("todo") as conn:
        cur=conn.cursor()
        cur.execute(sql_query)
        conn.commit()



def create_table():
    sql_query="""CREATE TABLE tasks(
        id INTEGER PRIMARY KEY,
        taskname TEXT,
        complete BOOLEAN,
        prioritize INTEGER
    );"""
    db_connection(sql_query)

def drop_table():
    sql_query= """DROP TABLE tasks """
    db_connection(sql_query)
    

if __name__ == "__main__":
    drop_table()
    create_table()