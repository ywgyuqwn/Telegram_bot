import telebot
from telebot import types

from nedelya import curr_week_for_bd, curr_week
from bd import get_day_formatting, get_week_formatting

token = '5739825141:AAFjcpyJPvb0EsyedNtz99S9RA8QJ8JjpDw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("/help", "/monday", "/tuesday", "/wednesday", "/thursday", "/friday", "/saturday","/currentweek", "/nextweek")
    mess = f'Здравствуйте, <em>{message.from_user.first_name}</em>!\nЯ бот с расписанием' \
           f'\nНапишите /help, чтобы посмотреть список команд.'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='Напишите /week - чтобы узнать, какая сейчас неделя'
                                           '\nНапишите /mtuci - для того, чтобы попасть на сайт МТУСИ'
                                           '\nУ меня есть такие команды:'
                                           '\n/monday - расписание на понедельник'
                                           '\n/tuesday - на вторник '
                                           '\n/wednesday - на среду '
                                           '\n/thursday - на четверг '
                                           '\n/friday - на пятницу '
                                           '\n/saturday - на субботу '
                                           '\n/currentweek - на текущую неделю '
                                           '\n/nextweek - на следующую неделю')


@bot.message_handler(commands=['week'])
def help(message):
    bot.send_message(message.chat.id, text=f'Сейчас {curr_week()} неделя')


@bot.message_handler(commands=['mtuci'])
def help(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить оффициальный сайт МТУСИ', url='https://mtuci.ru/'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['monday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 1))}', parse_mode='HTML')


@bot.message_handler(commands=['tuesday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 2))}', parse_mode='HTML')


@bot.message_handler(commands=['wednesday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 3))}', parse_mode='HTML')


@bot.message_handler(commands=['thursday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 4))}', parse_mode='HTML')


@bot.message_handler(commands=['friday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 5))}', parse_mode='HTML')


@bot.message_handler(commands=['saturday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 6))}', parse_mode='HTML')


@bot.message_handler(commands=['currentweek'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_week_formatting(curr_week_for_bd(1)))}', parse_mode='HTML')


@bot.message_handler(commands=['nextweek'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_week_formatting(curr_week_for_bd(1)))}', parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, text='Я вас не понимаю, введите /help для просмотра списка команд')


bot.polling(none_stop=True, interval=0)
