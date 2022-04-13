import telebot
from telebot import types

bot = telebot.TeleBot('5136259122:AAGyUYo1dH80vnRMh726bXBqLwODQQSL4U8')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "❕Здравствуйте меня зовут Айдар, и я создатель этого бота.\n" +
                     "Этот бот предназначен для того чтобы, делиться товарами с рынка Дордой.\n" +
                     "❕Этот бот хранит в себе данные о категориях\n" +
                     "❕По любым вопросам можете написать мне на \n" +
                     "WhatsApp: +996502215034")
    markup = types.ReplyKeyboardMarkup()
    mujod = types.KeyboardButton("Мужская одежда")
    jenod = types.KeyboardButton("Женская одежда")
    detod = types.KeyboardButton("Детская одежда")
    optom = types.KeyboardButton("Товары оптом")
    markup.add(mujod, jenod, detod, optom)
    bot.send_message(message.chat.id, "Выберите", reply_markup=markup)


@bot.message_handler()
def commandser(message):
    if message.text == "Мужская одежда":
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Футболки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Обувь", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Кофты", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1,btn2,btn3)

        btn1 = types.InlineKeyboardButton("Рубашки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Джинсы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Пиджаки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Спортивная одежджа", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Костюмы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Кардиганы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Водолазки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Галстуки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Ремни", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выберите", reply_markup=markup)

    if message.text == "Женская одежда":
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Платья", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Футболки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Пальто", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Кардиганы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Обувь", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Костюмы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Свиттеры", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Тренчи", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Брюки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Сумки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Блузы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Водолазки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Юбки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Джинсы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn3 = types.InlineKeyboardButton("Куртки", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2, btn3)

        btn1 = types.InlineKeyboardButton("Топы", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        btn2 = types.InlineKeyboardButton("Туники", url="https://t.me/+a_AlIPxtPKhlN2Ji")
        markup.row(btn1, btn2)


        bot.send_message(message.chat.id, "Выберите", reply_markup=markup)

bot.polling(none_stop=True)
