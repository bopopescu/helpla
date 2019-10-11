import telepot
import csv
from pprint import pprint
import database as dbb
import datetime as datetime
import os.path
import time

#Definining fun_stuff
token = "964928453:AAFiGYtt7oUGzF4tSl59wMW7yE0VdhcW_lg"
TelegramBot = telepot.Bot(token)



#Defining FUnctions

def format_date(date_Str):
    date_obj= date_Str.strip().split("-")
    if len(date_obj) == 1:
        if date_obj[0] == "today":
            return date.today()
        elif date_obj[0] == "tmrw":
            return datetime.date.today() + datetime.timedelta(days=1)
    #FIrst case: We have specific wrods
    elif len(date_obj) == 2:
    #Second case : We have DD-MM
        now = datetime.datetime.now()
        date = "-".join(date_obj) + str(now.year) + "2019 23:59"
        date_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M')
    #Third-Case we have DD-MM-YY
    elif len(date_obj) == 3:
        date = "-".join(date_obj).strip()
        date_obj = datetime.datetime.strptime(date, '%d-%m-%Y')
    return date_obj

def add_task(i):
    user_id = int(i['message']['from']['id'])
    name = i['message']["from"]["first_name"]
    task = i['message']['text'].split(',')
    chat_id = i['message']['chat']["id"]
    update_id = i['update_id']
    print("The Update id is "+str(update_id))
    if(dbb.check_user(user_id)):
        pass
    else:
        dbb.create_user(user_id,name,update_id)
    print(task[2])
    date = format_date(task[2])
    print(date)
    dbb.create_task(user_id, task[1],date,update_id)
    TelegramBot.sendMessage(chat_id, "Your Task <<{}>> has been added!".format(task[1]))

#TO_DO : ADD A REMOVAL FUNCTION
def remove_task(i):
    pass

def show_tasks(chat_id):
    tasks = dbb.get_tasks()
    TelegramBot.sendMessage(chat_id,
    "Your *Current Tasks* are : \n "+tasks, parse_mode= "Markdown")

def main():
    #We grab data from the telegram bot and find all of our latest tasks that we have sent in
    update_id = dbb.get_user_latest_id()
    user = 0
    print("We have initialised the update_id to be {}".format(update_id))
    updates = TelegramBot.getUpdates(update_id)
    #We then format the updates we recieve. They will be passed in using the
    #<Name> , <Deadline>
    for i in updates:
        pprint(i)
        command = i['message']['text']
        chat_id = i['message']['chat']["id"]
        user = int(i['message']['from']['id'])
        if command == '/get_tasks':
            show_tasks(chat_id)
        elif command == '/start':
            TelegramBot.sendMessage(chat_id,
            "Welcome to the *HelpLa Bot*! I was created to help deal with the huge chunk of to-dos that we need to work with in our day to day life \n Here is how to use the bot \n 1. To Add a To-Do Item, simply write it in as such *Task*,*Name Of Task*,*Deadline* \n 2. To get a list of current items, use the command \\get_tasks ",parse_mode='Markdown')
        else:
            add_task(i)
        update_id = i['update_id']

        user_id = user_id = int(i['message']['from']['id'])
        dbb.update_user_update_id(update_id,user_id)
        print("The new user ID is {}".format(dbb.get_user_latest_id()))

    dbb.update_user_update_id(dbb.get_user_latest_id()+1, user)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(30)
