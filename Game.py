import telebot
import random
#from telegram import ReplyKeyboardMarkup

token = '2047997961:AAEDUJwEeYiOQRXAXK_W0cff8gr1MIssl0M'
bot = telebot.TeleBot(token)

keyboard_game = telebot.types.ReplyKeyboardMarkup(True)
keyboard_game.row('кинжал', 'броня', 'щит', 'меч', 'лук')
keyboard_game.row('Завершить игру')

keyboard_menu = telebot.types.ReplyKeyboardMarkup(True)
keyboard_menu.row('Начать сражение', 'Правила')

keyboard_choice = telebot.types.ReplyKeyboardMarkup(True)
keyboard_choice.row('Да', 'Нет')


def send(id, text):
    bot.send_message(id, text)


def send_choice(id, text):
    bot.send_message(id, text, reply_markup=keyboard_choice)


def send_game(id, text):
    bot.send_message(id, text, reply_markup=keyboard_game)


def send_menu(id, text):
    bot.send_message(id, text, reply_markup=keyboard_menu)


@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text
    player_name = message.from_user.username
    if msg.lower() == '/start':
        send_choice(id, 'Здравствуй, {0}, ты готов к сражению со мной?'.format(player_name))
    if msg == 'Да':
        send_menu(id, 'Что ж, в таком случае добро пожаловать на арену')
    if msg == 'Нет':
        send_choice(id, 'Обдумай свой выбор, {0}'.format(player_name))
    if msg == 'Правила':
        send_menu(id,
                  'Игра является чуть усложненной версией классической игры "Камень, ножницы, бумага", так что это царство великого рандома.')
        send_menu(id, 'На выбор игроку дается 5 предметов: кинжал, броня, щит, меч и лук.')
        send_menu(id,
                  'Кинжал победит броню и щит, но проиграет мечу и луку. Броня одолеет щит и лук, но потерпит поражение от кинажала и меча')
        send_menu(id,
                  'Щит способен одолеть меч и лук, но проиграет кинжалу и броню. Меч победит кинжал и броню, но проиграет щиту и луку. ')
        send_menu(id, 'Лук хорош против кинжала и меча, но не выдержит натиска брони и щита')
        send_menu(id, 'Ничья присуждается в случае одинаковой экипировки')
    if msg == 'Начать сражение':
        send_game(id, 'Выбирай свое оружие, {0}'.format(player_name))

    def dagger(y):
        if y == 'броня' or y == 'щит':
            send_game(id, 'За тобой победа, внезапный удар кинжалом я не мог предусмотреть')
        elif y == 'меч' or y == 'лук':
            send_game(id, 'Ты проиграл, {0}'.format(player_name))
        else:
            send_game(id, 'В этот раз ничья')

    def armor(y):
        if y == 'щит' or y == 'лук':
            send_game(id, 'За тобой победа, выбрать броню было мудрым решением')
        elif y == 'кинжал' or y == 'меч':
            send_game(id, 'Ты проиграл, удача на моей стороне')
        else:
            send_game(id, 'В этот раз ничья')

    def shield(y):
        if y == 'меч' or y == 'лук':
            send_game(id, 'За тобой победа, я был бессилен против щита')
        elif y == 'кинжал' or y == 'броня':
            send_game(id, 'Ты проиграл на этот раз')
        else:
            send_game(id, 'В этот раз ничья')

    def sword(y):
        if y == 'кинжал' or y == 'броня':
            send_game(id, 'За тобой победа, ты слишком хорош в обращении мечом')
        elif y == 'щит' or y == 'лук':
            send_game(id, 'Ты проиграл, удача отвернулась от тебя')
        else:
            send_game(id, 'В этот раз ничья')

    def bow(y):
        if y == 'кинжал' or y == 'меч':
            send_game(id, 'За тобой победа, твоей меткости позавидует сам Леголас')
        elif y == 'броня' or y == 'щит':
            send_game(id, 'Ты проиграл, эльф из тебя никакущий')
        else:
            send_game(id, 'В этот раз ничья')

    items = ['кинжал', 'броня', 'щит', 'меч', 'лук']
    if msg in items:
        y = random.choice(items)
        send_game(id, y)
        if msg.lower() == 'кинжал':
            dagger(y)
        if msg.lower() == 'броня':
            armor(y)
        if msg.lower() == 'щит':
            shield(y)
        if msg.lower() == 'меч':
            sword(y)
        if msg.lower() == 'лук':
            bow(y)
    if msg == 'Завершить игру':
        send_menu(id, 'Отличное сражение вышло, {0}'.format(player_name))


bot.polling(none_stop=True)
