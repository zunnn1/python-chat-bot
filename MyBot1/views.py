from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

import telebot
import requests
import time


filename = "../beetroot_reply.txt"
my_file = open(filename, mode='a', encoding='utf-8')
token = ''

bot = telebot.TeleBot(token)


def log(message):
    print('\n____________')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1}. id = {2}\nТекст = {3}\n'.format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))


def add(message):
    from datetime import datetime
    my_file.write('\n{0}\nСообщение от {1} {2}.\nUser Nickname = @{3}\nТекст = {4}\n'.format(datetime.now(),
                                                                                            message.from_user.first_name,
                                                                                            message.from_user.last_name,
                                                                                            message.from_user.username,
                                                                                            message.text))


def command_log(message):
    my_file.write('\n{0} {1}'.format(message.from_user.first_name, message.from_user.last_name))


print(bot.get_me())
print(requests.__version__)


@bot.message_handler(commands=['start'])
def reply_start (message):
    bot.reply_to(message, 'Привет :) \nДля отправки отзыва используй команду /submit \nДля отправки анонимного отзыва используй команду /anon \nTвой User ID, First & Last name не будут записаны.')
    command_log(message)
    my_file.write('\nCommand "start"')
    log(message)


@bot.message_handler(commands=['submit'])
def reply_submit (message):
    bot.reply_to(message, 'Здесь ты можешь оставить отзыв не анонимно')
    command_log(message)
    my_file.write('\nCommand "submit"')
    log(message)


@bot.message_handler(commands=['anon'])
def reply_anon(message):
    bot.reply_to(message, 'Здесь ты можешь оставить анонимный отзыв')
    command_log(message)
    my_file.write('\nCommand "anon"')
    log(message)


@bot.message_handler(func=lambda m: True)
def reply_message(message):
    bot.reply_to(message, 'Спасибо за оставленный отзыв =)')
    log(message)
    add(message)


bot.polling(none_stop=False, interval=0, timeout=180)
my_file.close()


while True:
    bot.send_message(chat_id=196134493, text='Все в порядке, я работаю')
    bot.send_message(chat_id=398260592, text='Все в порядке, я работаю')
    time.sleep(3600)


