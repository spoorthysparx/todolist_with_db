import sqlite3

def insert_into_task_table(task,priority):
    sql_insert_query="""INSERT INTO tasks(taskname,complete,prioritize) VALUES ("%s",%s,"%s")""" % (task,0,priority)
    execute_query(sql_insert_query)


def execute_query(sql_query):
    with sqlite3.connect("todo") as conn:
        cur=conn.cursor()
        result=cur.execute(sql_query)
        conn.commit()
    return result

def select_incomplete_records():
    sql_select_query="""SELECT taskname,prioritize FROM tasks WHERE complete==0 ORDER BY prioritize DESC"""
    result=execute_query(sql_select_query).fetchall()
    return [x for x in result]

def select_completed_records():
    sql_select_query="""SELECT taskname,prioritize FROM tasks WHERE complete==1 ORDER BY prioritize DESC"""
    result=execute_query(sql_select_query).fetchall()
    return [x for x in result]


def mark_task_as_complete(task):
    sql_update_query="""UPDATE tasks SET complete=1 WHERE taskname="%s"AND complete=0"""%(task)
    execute_query(sql_update_query)

def update_task(old_task,new_task):
    sql_modify_query="""UPDATE tasks SET taskname = "%s" WHERE taskname == "%s" """%(new_task,old_task)
    execute_query(sql_modify_query)

if __name__ == "__main__":
    select_all_records()

