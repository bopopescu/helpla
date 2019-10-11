import mysql.connector as mysql
import datetime


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
    cursor.execute("CREATE TABLE tasks (update_id INT(11) PRIMARY KEY, task_name VARCHAR(255), Deadline DATETIME, user INT(11))")
    cursor.execute("CREATE TABLE users (id INT(11) PRIMARY KEY, Name VARCHAR(255), last_update_id INT(11))")
    cursor.close()

def get_user_latest_id():
    cursor = db.cursor(buffered = True)
    cursor.execute("SELECT last_update_id FROM users")
    user = cursor.fetchall()
    return user[0][0]

def update_user_update_id(update_Id,user_Id):
    cursor = db.cursor(buffered = True)
    currID = get_user_latest_id()
    if update_Id > currID:
        query = "UPDATE users SET last_update_id = {} WHERE id = {}".format(str(update_Id),str(user_Id))
        cursor.execute(query)
        db.commit()
        cursor.close()
        print("User ID Updated")
    else:
        print("User ID not updated")

update_user_update_id(3992779,155624230)

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

def create_user(user_id,user_name,update_Id):
    cursor = db.cursor(buffered=True)
    query = "INSERT INTO users (id, Name,last_update_id) VALUES (%s, %s,%s)"
    values = (user_id, user_name,update_Id)
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

def check_task(up_id):
    cursor = db.cursor(buffered= True)
    query = "SELECT * FROM tasks WHERE update_id ="+str(up_id)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    if len(result)==1:
        return True
    else:
        return False

def create_task(user_id,task_name, deadline,up_id):
    if check_task(up_id):
        print("Tasks Exists")
        pass
    else:
        cursor = db.cursor(buffered=True)
        #Defining Query
        query = "INSERT INTO tasks (update_id,user,task_name, Deadline) VALUES (%s,%s,%s, %s)"
        ## storing values in a variable
    
        values = (str(up_id),str(user_id), task_name, deadline)
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

def get_tasks():
    cursor = db.cursor(buffered = True)
    cursor.execute("SELECT task_name, Deadline FROM tasks")
    tasks = cursor.fetchall()
    sumTasks = "\n"
    count = 1
    for task in tasks:
        name = task[0]
        deadline = task[1].strftime('%m/%d/%Y')
        sumTasks += "{}. {} ( Deadline: {} )\n".format(count,name, deadline)
        count+=1
    sumTasks+="\n"
    return sumTasks

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
