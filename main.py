import telebot
import requests
import json
import sqlite3
import random
import datetime

win10ProPrice = 250
win10HomePrice = 300
off16Price = 290

QIWI_TOKEN = 'aeb2480de5814b00f4ffe8b4272d3e04'
QIWI_ACCOUNT = '+79138653949'
while True:
    try:
        status = '❌Не оплачено'
        bot = telebot.TeleBot('1398903140:AAFIMM6N_gzOTOt91jdlHqs4Ka6wyYESwtA')
        keyboardStart = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardStart.row('Ключи🔑', 'Помощь⚙')


        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id,
                             'Привет!\nЗдесь ты можешь купить ключ для Windows 10 или MS Office' + u'\U0001F609',
                             reply_markup=keyboardStart)


        keyboardBuy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardBuy.row('Купить💸', 'Выход❌')

        keyboardChose = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardChose.row('✅Windows 10 Pro')
        keyboardChose.row('✅Windows 10 Home')
        keyboardChose.row('✅Office 2016')
        keyboardChose.row('Выход❌')

        keyboardExit = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardExit.row('Выход❌')


        @bot.message_handler(content_types=['text'])
        def text_message(message):
            if message.text.lower() == 'помощь⚙':
                bot.send_message(message.chat.id, 'По всем вопросам пишите сюда: \n'
                                                  '@werfwes')


            elif message.text.lower() == 'ключи🔑':
                msg = 'Категории: \n' \
                      '➖➖➖Windows➖➖➖\n' \
                      '    🔐Windows 10 Pro \n' \
                      '                  ➡' + str(win10ProPrice) + ' руб. | ' + str(sum(1 for line in open('Win10ProKeys.txt', 'r'))) + ' шт.' + '\n' \
                      '    🔐Windows 10 Home \n' \
                      '                  ➡' + str(win10HomePrice) + ' руб. | ' + str(sum(1 for line in open('Win10HomeKeys.txt', 'r'))) + ' шт.' + '\n' \
                      '➖➖➖Office➖➖➖\n' \
                      '    🔐Office 2016 \n' \
                      '                  ➡' + str(off16Price) + ' руб. | ' + str(sum(1 for line in open('Off16Keys.txt', 'r'))) + ' шт.'
                bot.send_message(message.chat.id, msg, reply_markup=keyboardBuy)


            elif message.text.lower() == 'выход❌':
                bot.send_message(message.chat.id,
                                 'Привет!\nЗдесь ты можешь купить ключ для Windows 10 или MS Office' + u'\U0001F609',
                                 reply_markup=keyboardStart)

            elif message.text.lower() == 'купить💸':
                bot.send_message(message.chat.id, 'Выбери товар', reply_markup=keyboardChose)


            elif message.text == '✅Windows 10 Pro':
                if sum(1 for line in open('Win10ProKeys.txt', 'r')) > 0:
                    markup = telebot.types.InlineKeyboardMarkup()
                    markup.add(telebot.types.InlineKeyboardButton(text='Проверить оплату', callback_data=3))
                    bot.send_message(message.chat.id, 'Оплата:', reply_markup=keyboardExit)

                    random_code = random.randint(1000000, 9999999)
                    conn = sqlite3.connect('db.db')
                    conn.execute("CREATE TABLE IF NOT EXISTS payment_query(user_id INTEGER, sum INTEGER, code INTEGER)")
                    conn.execute(
                        f"INSERT INTO payment_query VALUES({message.from_user.id}, {win10ProPrice}, {random_code})")
                    conn.commit()
                    conn.close()

                    bot.send_message(message.chat.id,
                                     f'Для оплаты переведите {str(win10ProPrice)} рублей на счет QIWI \n'
                                     f'Номер: {QIWI_ACCOUNT} \n'
                                     f'Kомментарий: {str(random_code)}')
                    bot.send_message(message.chat.id, f'Статус: {status}', reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, 'Нет в наличии, ожидайте пополнение :(')



            elif message.text == '✅Windows 10 Home':
                if sum(1 for line in open('Win10HomeKeys.txt', 'r')) > 0:
                    markup = telebot.types.InlineKeyboardMarkup()
                    markup.add(telebot.types.InlineKeyboardButton(text='Проверить оплату', callback_data=3))
                    bot.send_message(message.chat.id, 'Оплата:', reply_markup=keyboardExit)

                    random_code = random.randint(1000000, 9999999)
                    conn = sqlite3.connect('db.db')
                    conn.execute("CREATE TABLE IF NOT EXISTS payment_query(user_id INTEGER, sum INTEGER, code INTEGER)")
                    conn.execute(
                        f"INSERT INTO payment_query VALUES({message.from_user.id}, {win10HomePrice}, {random_code})")
                    conn.commit()
                    conn.close()

                    bot.send_message(message.chat.id,
                                     f'Для оплаты переведите {str(win10HomePrice)} рублей на счет QIWI \n'
                                     f'Номер: {QIWI_ACCOUNT} \n'
                                     f'Kомментарий: {str(random_code)}')
                    bot.send_message(message.chat.id, f'Статус: {status}', reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, 'Нет в наличии, ожидайте пополнение :(')


            elif message.text == '✅Office 2016':
                if sum(1 for line in open('Off16Keys.txt', 'r')) > 0:
                    markup = telebot.types.InlineKeyboardMarkup()
                    markup.add(telebot.types.InlineKeyboardButton(text='Проверить оплату', callback_data=3))
                    bot.send_message(message.chat.id, 'Оплата:', reply_markup=keyboardExit)

                    random_code = random.randint(1000000, 9999999)
                    conn = sqlite3.connect('db.db')
                    conn.execute("CREATE TABLE IF NOT EXISTS payment_query(user_id INTEGER, sum INTEGER, code INTEGER)")
                    conn.execute(
                        f"INSERT INTO payment_query VALUES({message.from_user.id}, {off16Price}, {random_code})")
                    conn.commit()
                    conn.close()

                    bot.send_message(message.chat.id,
                                     f'Для оплаты переведите {str(off16Price)} рублей на счет QIWI \n'
                                     f'Номер: {QIWI_ACCOUNT} \n'
                                     f'Kомментарий: {str(random_code)}')
                    bot.send_message(message.chat.id, f'Статус: {status}', reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, 'Нет в наличии, ожидайте пополнение :(')

            else:
                print(f'Unknown message:{message.text}')
                bot.send_message(message.chat.id, 'Не работает(')


        @bot.callback_query_handler(func=lambda call: True)
        def query_handler(call):

            if call.data == '3':
                conn = sqlite3.connect('db.db')
                s = requests.Session()
                s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
                parameters = {'rows': '50'}
                h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments',
                          params=parameters)
                req = json.loads(h.text)

                result = conn.execute(
                    f"SELECT * FROM payment_query WHERE user_id = {call.message.chat.id}").fetchone()  # достаем данные из таблицы

                random_code = result[2]
                sum = result[1]

                # проходимся циклом по словарю
                for i in range(len(req['data'])):
                    if req['data'][i]['comment'] == str(random_code) and req['data'][i]['sum']['amount'] == sum:
                        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

                        status = '✅Оплачено'
                        bot.edit_message_text(f'Статус: {status}', call.message.chat.id, call.message.message_id)

                        conn.execute(
                            f"DELETE FROM payment_query WHERE user_id = {call.message.chat.id}")  # удаляем временные данные из таблицы
                        print(f'succesful:{call.message.chat.id},{random_code}, {sum}, {datetime.datetime.now()}')  # Запись лога

                        # Выдача и удаление ключа из файла
                        # Поиск файла
                        filename = ''
                        if sum == win10ProPrice:
                            filename = 'Win10ProKeys.txt'
                        elif sum == win10HomePrice:
                            filename = 'Win10HomeKeys.txt'
                        elif sum == off16Price:
                            filename = 'Off16Keys.txt'

                        # Удаление строки
                        f = open(filename, "r+")
                        d = f.readlines()
                        key = d[0]
                        bot.send_message(call.message.chat.id, f'Ваш ключ:\n{key}')
                        f.seek(0)
                        for i in d:
                            if i != key:
                                f.write(i)
                        f.truncate()
                        f.close()


        bot.polling()
    except Exception as e:
        print(str(e))
