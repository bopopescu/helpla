import telepot
import csv
from pprint import pprint
from org_writer import write_to_org
from datetime import date
import os.path


def format_text(s):
    n = s.split(",")
    return n

#This forms the neccesary data
token = "964928453:AAFiGYtt7oUGzF4tSl59wMW7yE0VdhcW_lg"
TelegramBot = telepot.Bot(token)

#We first read the latest task_id from our data.py file
with open("data.txt","r") as start:
    current_id = int(start.read());

#We then
updates = TelegramBot.getUpdates(current_id)
tasks = []
for i in updates:
    temp = []
    temp.append(str(i["update_id"]))
    #We then proccess the string according to <Type> <Name> <Deadline> <Description> format
    full_chunk = i["message"]["text"]
    temp.extend(format_text(full_chunk))
    tasks.append(temp)

#We then store the latest task_ID in the data_file
current_id+=len(tasks)

with open("data.txt","w") as f:
    new_id = str(current_id)
    f.write(new_id)


#We check if the file we want to write to exists. If it does, we append to the existing file, otherwise, we create the file and write the tasks to a new file.
name = date.today().strftime("%d-%m") + ".csv"
check_path = "/Users/ivan/Documents/Personal/Raw_input_Telegram/csv/" + name
print(name)
method = "w"
if os.path.exists(check_path):
    method = "a"
else:
    method = "w"

with open(check_path,method) as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(tasks)

write_to_org();
