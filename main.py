import telebot
from telebot import types
bot = telebot.TeleBot('5860364435:AAHjf2uRUHajY-NHqFc9-eA-7n7PeogoQRo')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Меню')
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text= "Привіт,{0.first_name}! Я чат бот помічник Лебединського ЗЗСО І-ІІІ ступенів №6, домопожу вам дізнатися корисну інформацію натисни, Меню".format(message.from_user),reply_markup=markup)
@bot.message_handler(regexp="Меню")
def button(message):
    markup = types.InlineKeyboardMarkup( row_width=2)
    item =types.InlineKeyboardButton('Розклад дзвінків', callback_data='question1')
    item2=types.InlineKeyboardButton('Розклад уроків', callback_data='question2')
    item3=types.InlineKeyboardButton('Перейти на сайт закладу', callback_data='question3')
    item4=types.InlineKeyboardButton('Перейти в групу на фейсбуці', callback_data='question4')
    markup.add(item,item2,item3,item4)

    bot.send_message(message.chat.id,
                    text="Виберіть, що саме ви хочете переглянути", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'question1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='<b>1 урок</b>- 11.30-12.15,'
                                                                                                 '<b>2 урок</b> -12.25-13.10, '
                                                                                                 '<b>3 урок</b>-13.20-14.10,'
                                                                                                 '<b>4 урок</b>-14.20-15.05,'
                                                                                                 '<b>5 урок</b> -15.15-16.00,'
                                                                                                 '<b>6 урок</b>- 8.00-8.30,'
                                                                                                 '<b>7 урок</b> -8.50-9.35', parse_mode='html')

        elif call.data == 'question2':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton('5 клас', callback_data='розклад 5')
            item4 = types.InlineKeyboardButton('6 клас', callback_data='розклад 6')
            item5 = types.InlineKeyboardButton('7-А клас', callback_data='розклад 7-A')
            item6 = types.InlineKeyboardButton('7-Б клас', callback_data='розклад 7-Б')
            item7 = types.InlineKeyboardButton('8-А клас', callback_data='розклад 8-А')
            item8 = types.InlineKeyboardButton('8-Б клас', callback_data='розклад 8-Б')
            item9 = types.InlineKeyboardButton('9-А клас', callback_data='розклад 9-А')
            item10 = types.InlineKeyboardButton('9-Б клас', callback_data='розклад 9-Б')
            markup.add(item3,item4,item5,item6,item7,item8,item9,item10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Виберіть клас', reply_markup=markup)
        elif call.data == 'question3':
            markup = types.InlineKeyboardMarkup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='https://lebedyn6.school.org.ua/')

        elif call.data == 'question4':
            markup = types.InlineKeyboardMarkup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='https://www.facebook.com/groups/194011261157082')

        if call.data == 'розклад 5':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item11 = types.InlineKeyboardButton('Понеділок', callback_data='понеділок')
            item12 = types.InlineKeyboardButton('Вівторок', callback_data='вівторок')
            item13 = types.InlineKeyboardButton('Середа', callback_data='середа')
            item14 = types.InlineKeyboardButton('Четвер', callback_data='четвер')
            item15 = types.InlineKeyboardButton('Пятниця', callback_data='п_ятниця')
            markup.add(item11,item12,item13,item14,item15)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Виберіть день тижня', reply_markup=markup)


        if call.data == 'понеділок':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='<b>1 урок</b>-Математика,'
                                                                                                 '<b>2 урок</b>-Англійська мова,'
                                                                                                 '<b>3 урок</b>- Основи здоров_я,'
                                                                                                 '<b>4 урок</b>-Історія, '
                                                                                                 '<b>5 урок</b>-Українська література',parse_mode='html')
        if call.data == 'вівторок':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Українська мова,'
                                       '<b>2 урок</b>-Пізнаємо природу,'
                                       '<b>3 урок</b>- Математика,'
                                       '<b>4 урок</b>-Англійська мова, '
                                       '<b>5 урок</b>-Українська література', parse_mode='html')
        if call.data == 'середа':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Математика,'
                                       '<b>2 урок</b>-Інформатика/Технології,'
                                       '<b>3 урок</b>- Українська мова,'
                                       '<b>4 урок</b>-Зарубіжна література, '
                                       '<b>5 урок</b>-Інформатика/Технології', parse_mode='html')
        if call.data == 'четвер':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Пізнаємо природу,'
                                       '<b>2 урок</b>-Українська мова,'
                                       '<b>3 урок</b>- Фізкультура,'
                                       '<b>4 урок</b>-Образотворче мистецтво, '
                                       '<b>5 урок</b>-Математика,'
                                       '<b>6 урок</b> - Музичне мистецтво', parse_mode='html')
        if call.data == 'п_ятниця':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Математика,'
                                       '<b>2 урок</b>-Українська мова,'
                                       '<b>3 урок</b>- Інформатика/Технології,'
                                       '<b>4 урок</b>-Англійська мова, '
                                       '<b>5 урок</b>-Інформатика/Технології,'
                                       '<b>6 урок</b> - Фізична культура', parse_mode = 'html')




        if call.data == 'розклад 6':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item16 = types.InlineKeyboardButton('Понеділок', callback_data='понеділок1')
            item17 = types.InlineKeyboardButton('Вівторок', callback_data='вівторок1')
            item18 = types.InlineKeyboardButton('Середа', callback_data='середа1')
            item19= types.InlineKeyboardButton('Четвер', callback_data='четвер1')
            item20 = types.InlineKeyboardButton('Пятниця', callback_data='п_ятниця1')
            markup.add(item16,item17,item18,item19,item20)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Виберіть день тижня', reply_markup=markup)

        if call.data == 'понеділок1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Українська мова,'
                                                                                                 '<b>2 урок</b>- Математика,'
                                                                                                 '<b>3 урок</b>-Англійська мова,'
                                                                                                 '<b>4 урок</b>-Основи здоров_я,'
                                                                                                 '<b>5 урок</b> - Зарубіжна література, '
                                                                                                 '<b>6 урок </b> -Вчимося жити разом,'
                                                                                                 ' <b>7 урок </b>-Технології(1)', parse_mode = 'html')
        if call.data == 'вівторок1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Матемитика,'
                                       '<b>2 урок</b>-Українська мова,'
                                       '<b>3 урок</b>- Географія,'
                                       '<b>4 урок</b>-Українська література, '
                                       '<b>5 урок</b>-Англійська мова,'
                                       '<b>6 урок</b>-Історія, '
                                       '<b>7 урок</b>-Фізична культура', parse_mode=')html')
        if call.data == 'середа1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Пізнаємо природу,'
                                       '<b>2 урок</b>-Історія,'
                                       '<b>3 урок</b>- Інформатика/Технології,'
                                       '<b>4 урок</b>-Українська мова, '
                                       '<b>5 урок</b>-Фізична культура'
                                       '<b>6 урок</b>-Математика, '
                                       '<b>7 урок</b>-Технології2', parse_mode='html')
        if call.data == 'четвер1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Інформатика/Технології,'
                                       '<b>2 урок</b>-Математика,'
                                       '<b>3 урок</b>- Пізнаємо природу,'
                                       '<b>4 урок</b>-Фізична культура, '
                                       '<b>5 урок</b>-Образотворче мистецтво,'
                                       '<b>6 урок</b> - Зарубіжна література', parse_mode='html')
        if call.data == 'п_ятниця1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='<b>1 урок</b>-Українська мова,'
                                       '<b>2 урок</b>-Геграфія,'
                                       '<b>3 урок</b>- Англійська мова,'
                                       '<b>4 урок</b>-Математика, '
                                       '<b>5 урок</b>-Українська література,'
                                       '<b>6 урок</b> - Музичне мистецтво', parse_mode = 'html')


bot.polling(none_stop=True)