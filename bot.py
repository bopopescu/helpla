import telepot
import csv
from pprint import pprint
import database as dbb
from datetime import date
import os.path

#Definining fun_stuff
token = "964928453:AAFiGYtt7oUGzF4tSl59wMW7yE0VdhcW_lg"
TelegramBot = telepot.Bot(token)

#We grab data from the telegram bot and find all of our latest tasks that we have sent in
updates = TelegramBot.getUpdates(3992767)
#We then format the updates we recieve. They will be passed in using the
#<Name> , <Deadline>
for i in updates:
    user_id = int(i['message']['from']['id'])
    name = i['message']["from"]["first_name"]
    task = i['message']['text'].split(',')
    print(user_id)
    print(dbb.check_user(user_id))
    if(dbb.check_user(user_id)):
        pass
    else:
        dbb.create_user(user_id,name)
    dbb.create_task(user_id, task[1],task[2])
    dbb.show_tasks()



# for i in updates:
#     temp = []
#     temp.append(str(i["update_id"]))
#     #We then proccess the string according to <Type> <Name> <Deadline> <Description> format
#     full_chunk = i["message"]["text"]
#     temp.extend(format_text(full_chunk))
#     tasks.append(temp)
# #We then store the latest task_ID in the data_file
# current_id+=len(tasks)
#
# with open("data.txt","w") as f:
#     new_id = str(current_id)
#     f.write(new_id)
#
#
# #We check if the file we want to write to exists. If it does, we append to the existing file, otherwise, we create the file and write the tasks to a new file.
# name = date.today().strftime("%d-%m") + ".csv"
# check_path = "/Users/ivan/Documents/Personal/Raw_input_Telegram/csv/" + name
# print(name)
# method = "w"
# if os.path.exists(check_path):
#     method = "a"
# else:
#     method = "w"
#
# with open(check_path,method) as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(tasks)
#
# write_to_org();
