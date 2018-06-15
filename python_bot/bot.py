#!/usr/bin/python3

import asyncio
import requests
import json

import telebot

TELEGRAM_BOT_TOKEN = "token"                # Токен telegram-бота.

DISCORD_BOT_TOKEN = "token"                 # Токен discord-бота.
DISCORD_CHANNEL_ID = "449635071453036554"                                           # ID дискорд канала
                                                                                   # url отправки сообщений
DISCORD_API_URL = "https://discordapp.com/api/channels/{}/messages".format(DISCORD_CHANNEL_ID)

headers = {"Authorization":"Bot {}".format(DISCORD_BOT_TOKEN),  # Заголовок POST запроса
           "Content-Type":"application/json"}

telegram_help_info = { "start" : "(Start, START, st) - Начать работу",
                       "help" : "(Help, HELP) - Вывести справку",
                       "stop" : "(Stap, STOP) - Приостановить работу",
                       "helo" : "(Hello, HELLO) -Приветствие" }
is_bot_start = False 


def listener(messages):
    for message in messages:
        if message.content_type == 'text':
            print(str(message.chat.first_name) + " [id:" + str(message.chat.id) + "]: " + message.text)

telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
telegram_bot.set_update_listener(listener)

@telegram_bot.message_handler(commands=['start', 'Start', 'START', 'st'])
def start(message):
    """
    Начало работы бота. 
    """
    global is_bot_start 
    if not is_bot_start:
        is_bot_start = True 
        answer = "Бот начинает работу."
    else:
        answer = "Бот уже работает."

    telegram_bot.send_message(message.chat.id, answer)

@telegram_bot.message_handler(commands=['stop', 'Stop', 'STOP'])
def stop(message):
    """
    Приостановка работы бота.
    """
    global is_bot_start
    if is_bot_start:
        is_bot_start= False
        answer = "Работа бота приостановлена."
    else:
        answer = "Работа бота уже приостановлена"

    telegram_bot.send_message(message.chat.id, answer)

@telegram_bot.message_handler(commands=['help', 'Help', 'HELP', 'h'])
def help(message):
    """
    Выводит справку в чат.
    """
    answer = "Справка:\n"
    for key in telegram_help_info:
        answer += '/' + key + ' - ' + telegram_help_info[key] + '\n'
        
    telegram_bot.send_message(message.chat.id, answer)

@telegram_bot.message_handler(commands=['hello', 'Hello', 'HELLO', 'Hello!', 'hello!'])
def hello(message):
    """
    Бот просто здаровается.
    """
    telegram_bot.reply_to(message, "Привет!")

@telegram_bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    if is_bot_start:
        data = json.dumps({"content" : message.text})
        r = requests.post(DISCORD_API_URL, headers = headers, data = data)
        send_message_log(r)
    else:
        telegram_bot.send_message(message.chat.id, "Попробуйте /help")

def send_message_log(r):
    print("Попытка доставить сообщение...")
    print("Ответ сервера: ", r)
    print(r.text)


if __name__ == "__main__":
    telegram_bot.polling()
