import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "pass",
    database = "tasks"
)
def reset_tables():
    cursor = db.cursor()
    cursor.execute("DROP TABLE users")
    cursor.execute("DROP TABLE tasks")

#Run this if you are running python bot for the first time
def create_tables():
    cursor = db.cursor(buffered=True)
    cursor.execute("CREATE TABLE tasks (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), Deadline VARCHAR(255), user INT(11))")
    cursor.execute("CREATE TABLE users (id INT(11) PRIMARY KEY, Name VARCHAR(255))")
    cursor.close()

def check_user(user_Id):
    cursor = db.cursor(buffered=True)
    sql = "SELECT * FROM users WHERE id = %s"
    id = (str(user_Id),)
    cursor.execute(sql,id)
    result = cursor.fetchall()
    if len(result)==1:
        return True
    else:
        return False

def create_user(user_id,user_name):
    cursor = db.cursor(buffered=True)
    query = "INSERT INTO users (id, Name) VALUES (%s, %s)"
    values = (user_id, user_name)
    cursor.execute(query,values)
    db.commit()
    cursor.close()

def remove_user(user_id):
    cursor = db.cursor(buffered=True)
    query = "DELETE FROM users WHERE id = "+ str(user_id)
    cursor.execute(query)
    db.commit()
    cursor.close()

def show_users():
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    cursor.close()

def show_tasks():
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall() ## it returns list of tables present in the database
    ## showing all the tables one by one
    for task in tasks:
        print(task)
    cursor.close()

def create_task(user_id,task_name, deadline):
    cursor = db.cursor(buffered=True)
    #cursor.execute("CREATE TABLE tasks (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), Deadline VARCHAR(255))")
    ## defining the Query
    query = "INSERT INTO tasks (user,task_name, Deadline) VALUES (%s,%s, %s)"
    ## storing values in a variable
    values = (str(user_id), task_name, deadline)
    ## executing the query with values
    cursor.execute(query, values)
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()
    print(cursor.rowcount, "record inserted")
    cursor.close()

def show_tables():
    cursor = db.cursor(buffered=True)
    ## getting all the tables which are present in 'datacamp' database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall() ## it returns list of tables present in the database
    ## showing all the tables one by one
    for table in tables:
        print(table)
    cursor.close()

def get_user_tasks(user_id):
    cursor = db.cursor(buffered=True)
    ## defining the Query
    query = "SELECT task_name FROM tasks WHERE user = "+ user_id
    ## getting 'name', 'user_name' columns from the table
    cursor.execute(query)
    ## fetching all records from the 'cursor' object
    tasks = cursor.fetchall()
    cursor.close()
    return tasks


show_tasks()
