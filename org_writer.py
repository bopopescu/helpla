import PyOrgMode
from datetime import date
import os.path

def write_to_org():
    base = PyOrgMode.OrgDataStructure()
    day = date.today().strftime("%d-%m")
    name = day + ".org"
    check_path = "/Users/ivan/Documents/Personal/Raw_input_Telegram/todos/" + name
    tasks = []

    #We first check if the file exists within the To-Dos Folder. if it doesn't we create it. Else, we load the base file and read the items from it.
    if os.path.exists(check_path):
        base.load_from_file(check_path)
        with open(check_path,"r") as f:
            items = f.readlines()
            for i in range(len(items)):
                tasks.append(items[i][7:].strip().lower())
    else:
        base.load_from_file("template/org_mode_template.org")

    csv_path = "/Users/ivan/Documents/Personal/Raw_input_Telegram/csv/" + day + ".csv"
    print("We are reading from CSV path "+csv_path)
    #First we read from our CSV to extract our lists of tasks
    with open(csv_path,"r") as d:
        for line in d:
            line = line.split(",")
            task = line[2].lower().strip()
            print("We are now adding " + task)
            if task not in tasks:
                tasks.append(task)

    #We then Loop through the tasks array to append these tasks to our Output File for the day
    print("We now have our lists of tasks -->")
    print(tasks)

    with open(check_path,"w") as f:
        for i in tasks:
            f.write("* TODO "+i + "\n")

    base.save_to_file(name)
