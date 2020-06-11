import sqlite3

db = "my_todo.db"
table_name = "tasks"
conn = sqlite3.connect(db)
c= conn.cursor()


def create_table():
    sql = "Create table if not Exists " + table_name + " (ID Integer Primary key Autoincrement, TaskName text)"
    c.execute(sql)


def data_entry(task):
    sql="Insert into "+ table_name+"values(?)",[task]
    c.execute(sql)
    print("The task is added in the database")
    conn.commit()


def printData():
    sql="Select * from "+table_name
    c.execute(sql)


def deleteTask(index):
    sql="Delete from "+table_name+"where ID=?", (index, )
    c.execute(sql)
    print("Task is completed")


def closeCurser():
    c.close()
    conn.close()
