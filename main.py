import telebot
import DataBase
import mysql.connector
import GeneralMessages


token = "1195843130:AAGagMN1LxmrOV-eqr_wjIjdoWNIRAzv8h0"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, GeneralMessages.START_MSG)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, GeneralMessages.HELP_MSG)

@bot.message_handler(content_types = ['text'])
def send_text(message):
    if message.text.lower() == 'поиск по названию':
        msg = bot.send_message(message.chat.id, 'Введи название дорамы, котрую хочешь посмотреть(и мы попробуем её найти в нашей базе)')
        bot.register_next_step_handler(msg,process_title_search)
    elif message.text.lower() == 'поиск по жанру':
        msg = bot.send_message(message.chat.id, 'Введи нужные жанры(если несколько, то через запятую без пробелов)')
        bot.register_next_step_handler(msg, process_genre_search)
    elif message.text.lower() == 'поиск по актеру':
        msg = bot.send_message(message.chat.id,'Введи нужных актеров(если несколько, то через запятую без пробелов)')
        bot.register_next_step_handler(msg, process_actor_search)
    elif message.text.lower() == 'поиск по году':
        msg = bot.send_message(message.chat.id, 'Введи нужный год или диапазон годов(если вводишь диапазон, то вводи в формате год-год)')
        bot.register_next_step_handler(msg, process_year_search)
    elif message.text.lower() == 'случайная дорама':
        msg = bot.send_message(message.chat.id, 'Держи случайную дораму из нашей базы, надеемся что тебе понравится \n')
        information = DataBase.random_dorama()
        bot.send_message(message.chat.id, information)
    elif message.text.lower() == 'добавить в избранное':
        msg = bot.send_message(message.chat.id, 'Введи название дорамы, которую хочешь добавить')
        bot.register_next_step_handler(msg, process_add_to_favourites)
    elif message.text.lower() == 'избранное':
        try:
            connection = DataBase.get_connection()
            cursor = connection.cursor()
            user_id = message.from_user.id
            command2 = "SELECT name_of_movie FROM Favourites WHERE id_user LIKE '%" + str(
                user_id) + "%'"
            cursor.execute(command2)
            titles = cursor.fetchall()
            if len(titles) == 0:
                raise NameError('Ошибка')
            msg = bot.send_message(message.chat.id, 'Ваш список избранного: \n')
            information = DataBase.select_from_favourites(user_id)
            bot.send_message(message.chat.id, information)
        except Exception as e:
            bot.reply_to(message, "Ваш список пуст")
    elif message.text.lower() == 'удалить из избранного':
        msg = bot.send_message(message.chat.id, 'Введи название дорамы, которую хочешь удалить из избранного:')
        bot.register_next_step_handler(msg, process_delete_from_favourites)
    else:
        bot.send_message(message.chat.id, "Не понял вашей команды")

def process_add_to_favourites(message):
    try:
        connection = DataBase.get_connection()
        cursor = connection.cursor()
        user_id = message.from_user.id
        command2 = "SELECT name_of_movie FROM Favourites WHERE id_user LIKE '%" + str(user_id) + "%' AND name_of_movie LIKE '%" + message.text + "%'"
        cursor.execute(command2)
        titles = cursor.fetchall()
        if len(titles) > 0:
            raise NameError('Ошибка, уточните название дорамы')
        DataBase.add_to_favourites(user_id,message.text)
        bot.send_message(message.chat.id, "Дорама успешно добавлена")
    except Exception as e:
        bot.reply_to(message,"Такой дорамы не нашлось в базе данных или такая дорама уже есть в вашем списке(проверьте с помощью команды избранное")

def process_delete_from_favourites(message):
    try:
        connection = DataBase.get_connection()
        cursor = connection.cursor()
        user_id = message.from_user.id
        command2 = "SELECT name_of_movie FROM Favourites WHERE id_user LIKE '%" + str(
            user_id) + "%' AND name_of_movie LIKE '%" + message.text + "%'"
        cursor.execute(command2)
        titles = cursor.fetchall()
        if len(titles) == 0:
            raise NameError('Ошибка')
        DataBase.delete_from_favourites(user_id, message.text)
        bot.send_message(message.chat.id, "Дорама успешно удалена")
    except Exception as e:
        bot.reply_to(message, "Такой дорамы не нашлось в вашем списке избранного")

def process_genre_search(message):
    try:
        information = DataBase.genre_search(message.text)
        bot.send_message(message.chat.id, information)
    except Exception as e:
        bot.reply_to(message,"Таких жанров у нас не нашлось, либо не нашлось такой дорамы, введите команду и попробуйте снова")

def process_title_search(message):
    try:
        information = DataBase.title_search(message.text)
        bot.send_message(message.chat.id, information)
    except Exception as e:
        bot.reply_to(message, "Такой дорамы не нашлось в нашей базе данных")

def process_actor_search(message):
    try:
        information = DataBase.actor_search(message.text)
        bot.send_message(message.chat.id, information)
    except Exception as e:
        bot.reply_to(message, "Таких актеров не нашлось в нашей базе данных")

def process_year_search(message):
    try:
        information = DataBase.year_search(message.text)
        bot.send_message(message.chat.id, information)
    except Exception as e:
        bot.reply_to(message, "Проверьте диапазон годов или в нашей базе данных не нашлось дорам этого года")

def process_random_search(message):
    information = DataBase.random_dorama()
    bot.send_message(message.chat.id, information)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)