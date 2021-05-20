import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='bot.log', level=logging.INFO)

import settings
#настройка прокси
# PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
#     'urllib3_proxy_kwargs':{'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! ты вызвал команду /start')
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
def main():
    #Создаем бота и передаем ему ключ для авторизации на серверахтелеграмм
    mybot = Updater(settings.API_KEY, use_context=True)
    #, request_kwargs=PROXY)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    #Камандуем бота ходиить в телеграмм за сообщениями
    mybot.start_polling()
    #Запускаем бота, он будет работать пока мы его не остановим принудительно
    mybot.idle()

main()