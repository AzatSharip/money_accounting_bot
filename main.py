# -*- coding: utf-8 -*-
# https://docs.python-telegram-bot.org/en/stable/telegram.ext.jobqueue.html?highlight=run_once
import datetime
import pandas as pd
import os
import time
import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters
from threading import Thread

TOKEN = '1001253586:AAF0dtLaEu_RKkaVuJQVjb3rTF1jrmgJ4-I'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hello!")
    # print(update.effective_chat.id) 268653382

job = updater.job_queue
r = {'user1': 268653382}
print(datetime.time.now())


def once(context: CallbackContext):
    message = "Hello, this message will be sent only once"
    # send message to all users
    id = r['user1']
    context.bot.send_message(chat_id=id, text=message)

def to_time(context: CallbackContext):
    message = "It s time!"
    # send message to all users
    id = r['user1']
    context.bot.send_message(chat_id=id, text=message)




if __name__ == '__main__':
    start_handler = CommandHandler('start', start, run_async=True)
    dispatcher.add_handler(start_handler)

    job.run_once(once, 5)
    job.run_daily(to_time, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=12, minute=51, second=00))


    # get_city_name_from_user_handler = MessageHandler(Filters.text & (~Filters.command), get_city_name_from_user, run_async=True)
    # dispatcher.add_handler(get_city_name_from_user_handler)
    #
    # thread1 = Thread(target=second_process)
    # thread1.start()

    updater.start_polling()
    updater.idle()
