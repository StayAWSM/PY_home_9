import logging


from telebot import types
import telebot


bot = telebot.TeleBot('5932911207:AAF9tzJRdtoF-hOu83kUeIR3gHvKlUtNccA')


def filter_dialog(record: logging.LogRecord):
    if 'id' in record.getMessage():
        return record.getMessage()


logger = telebot.logger
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='bot_log.csv', encoding='UTF-8')
handler.setFormatter(logging.Formatter(fmt='[%(levelname)s: %(asctime)s] %(message)s'))
logger.addFilter(filter_dialog)
logger.addHandler(handler)


@bot.message_handler(commands=['start'])
def start(message):
    text_message1 = f'<b><i>Привет, {message.from_user.first_name}!</i></b> \U0001F600'
    text_message2 = f'Этот бот может оценить Ваше фото, если Вы его пришлёте, '\
                    f'подсказать Вам время и дату, а также поможет найти примеры моих работ.'
    markup = telebot.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Веб сайт')
    demo_audio = types.KeyboardButton('Демо аудиозапись')
    start = types.KeyboardButton('Start')
    help = types.KeyboardButton('Help')
    markup.add(website, start, demo_audio, help)
    bot.send_message(message.chat_id, text_message1, parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat_id, text_message2, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'веб сайт':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://vk.com'))
        markup.add(types.InlineKeyboardButton('Посетить сайт2', url='https://youtube.com'))
        bot.send_message(message.chat_id, 'Посетите сайт, созданный для примера', reply_markup=markup)
    elif get_message_bot == 'демо аудиозапись':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Прослушать аудиозапись', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        bot.send_message(message.chat_id, 'Тыкните, чтобы прослушать запись', reply_markup=markup)
    elif get_message_bot == 'start':
        start(message)
    else:
        bot.send_message(message.chat_id, 'Я Вас не понимаю. Нажмите, пожалуйста, на одну из кнопок ниже')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat_id, '0, классное фото!')


print('Бот работает')

bot.polling(none_stop=True)
