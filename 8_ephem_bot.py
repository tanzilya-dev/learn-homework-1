"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    print('Call /start')
    # print(update.message)
    # print(dir(update.message))
    user_name = update.message.from_user.first_name
    # print(user_name)
    update.message.reply_text(f'Hi, {user_name}! You called command /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_planet_constellation(update, context):
    planet_name = update.message.text.split()[1].capitalize()
    # print(planet_name)
    now = datetime.datetime.now()
    planet = getattr(ephem, planet_name)(now.strftime("%Y/%m/%d"))
    constell = ephem.constellation(planet)
    # print(constellation)
    update.message.reply_text(f'Today planet {planet_name} is in constellation {constell[1]}')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
