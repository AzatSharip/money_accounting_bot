TOKEN = '1001253586:AAF0dtLaEu_RKkaVuJQVjb3rTF1jrmgJ4-I'

import telegram
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обработчик команды /start
def start(update, context):
    reply_keyboard = [['Расход', 'Доход'], ['Перевод между счетами', 'Настройки']]
    update.message.reply_text(
        'Выберите действие:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    )

# Обработчик кнопок "Расход", "Доход", "Перевод между счетами" и "Настройки"
def handle_button(update, context):
    text = update.message.text

    if text == 'Расход':
        update.message.reply_text('Вы выбрали "Расход"')
    elif text == 'Доход':
        update.message.reply_text('Вы выбрали "Доход"')
        inline(update)
    elif text == 'Перевод между счетами':
        update.message.reply_text('Вы выбрали "Перевод между счетами"')
    elif text == 'Настройки':
        update.message.reply_text('Вы выбрали "Настройки"')

def inline(update):
    with open('buttons.json') as f:
        data = json.load(f)

    # Создаем кнопки на основе данных из JSON-файла
    buttons = []
    for button_data in data['income']:
        button = InlineKeyboardButton(button_data['label'], callback_data=button_data['callback'])
        buttons.append([button])


    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Выберите один из вариантов:', reply_markup=reply_markup)
    text = update.message.reply_text
    print(text)

# Создаем объект бота и добавляем обработчики
updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^(Расход|Доход|Перевод между счетами|Настройки)$'), handle_button))



# Запускаем бота
updater.start_polling()
updater.idle()

