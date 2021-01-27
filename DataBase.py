# -*- coding: utf-8 -*-
import mysql.connector
import random

def get_connection():
    connection = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
    )
    return connection



#connection = get_connection()
#cursor = connection.cursor()
#cursor.execute("CREATE DATABASE DoramaDB")
#cursor.execute("SHOW DATABASES")
#for x in cursor:
    #print(x)
def add_table_in_database(table_name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE {} (id int AUTO_INCREMENT PRIMARY KEY,name_of_movie VARCHAR(100) NOT NULL,year INT,number_of_episodes INT,genre varchar(100),actors varchar(200),description varchar(3000) not null,rating_of_movie float,link varchar(100))".format(table_name))
    cursor.execute("SHOW TABLES")

    for tb in cursor:
        print(tb)

#add_table_in_database("Favourites")
#add_table_in_database("doramalist")


def insert_into_table(table_name,user_id,first_name,last_name):
    connection = get_connection()
    cursor = connection.cursor()

    sqlInsert = "INSERT INTO {} (user_id,first_name,last_name) VALUES (%s,%s,%s)".format(table_name)
    user = (user_id,first_name,last_name)

    cursor.execute(sqlInsert,user)
    connection.commit()

    connection.close()

def cortege_parser(cortege1):
    result = ''
    cortege = list(cortege1)
    result += "Название фильма: " + cortege[1] + "\n" \
            "Год выпуска: " + str(cortege[2]) + "\n" \
            "Колличество эпизодов: " + str(cortege[3]) + "\n" \
            "Жанры фильма: " + cortege[4] + "\n" \
            "Актеры в главных ролях: " + cortege[5] + "\n" \
            "Описание фильма: " + cortege[6] + "\n" \
            "Рейтинг фильма: " + str(cortege[7]) + "\n" \
            "Ссылка на фильм: " +  cortege[8] + "\n" \
            "\n"
    return (result)

def add_to_favourites(user_id,str1):
    connection = get_connection()
    cursor = connection.cursor()
    command = "Select name_of_movie FROM doramalist WHERE name_of_movie LIKE '%" + str1 + "%' "
    cursor.execute(command)
    titles = cursor.fetchall()
    for title in titles:
        if len(titles) == 1:
            cortege = list(title)
            command1 = "INSERT INTO Favourites (id_user,name_of_movie) VALUES (%s,%s)"
            inserted = (user_id,str(cortege[0]))
            cursor.execute(command1,inserted)
            connection.commit()
            connection.close()

def select_from_favourites(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    result = 'Избранные дорамы: \n'
    i = 1
    command = "Select name_of_movie FROM Favourites WHERE id_user LIKE '%" + str(user_id) + "%'"
    cursor.execute(command)
    titles = cursor.fetchall()
    for title in titles:
        cortege = list(title)
        result += str(i) + ". " + cortege[0] + "\n"
        i = i + 1
    return (result)

def delete_from_favourites(user_id,message):
    connection = get_connection()
    cursor = connection.cursor()
    command = "DELETE FROM Favourites WHERE id_user LIKE '%" + str(user_id) + "%' AND name_of_movie LIKE '%" + message + "%'"
    cursor.execute(command)
    connection.commit()

def genre_search(message):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    i = 0
    parser = []
    #message.replace(" ,", "")
    message = ''.join(message.split())
    parser = message.split(",")
    command = "Select * FROM doramalist WHERE genre LIKE '%" + parser[0] + "%' "
    if len(parser) == 0:
        return("Дорам по данному жанру у нас не нашлось или такого жанра у нас нету.")
    if len(parser) > 1:
        for genre in parser:
            if i == 0:
                i = i + 1
                continue
            command += "AND genre LIKE '%" + parser[i] + "%'"
            i = i + 1
    cursor.execute(command)
    genres = cursor.fetchall()
    i = 1
    if (len(genres) > 0):
        result += "Список фильмов по жанру: \n"
        for genre in genres:
            result += str(i) + ". " + genre[1] + "\n"
            i = i + 1
    return (result)

def title_search(str):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    command = "Select * FROM doramalist WHERE name_of_movie LIKE '%" + str + "%' "
    cursor.execute(command)
    titles = cursor.fetchall()
    for title in titles:
        result += cortege_parser(title)
    return(result)

def actor_search(str):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    i = 0
    list = []
    str.replace(', ',',')
    list = str.split(",")
    command = "Select * FROM doramalist WHERE actors LIKE '%" + list[0] + "%' "
    if len(list) > 1:
        for actor in list:
            if i == 0:
                i = i + 1
                continue
            command += "AND actors LIKE '%" + list[i] + "%'"
            i = i + 1
    cursor.execute(command)
    actors = cursor.fetchall()
    for actor in actors:
        result += cortege_parser(actor)
    return(result)

def year_search(str1):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    i = 0
    list = []
    str1.replace(' ','')
    list = str1.split("-")
    if len(list) == 1:
        command = "Select * FROM doramalist WHERE year = " + list[i]
    if len(list) > 1:
        if list[0] < list[1]:
            command = "Select * FROM doramalist WHERE year >= '" + list[i] + "' AND year <= '" + list[i+1] + "'"
    cursor.execute(command)
    years = cursor.fetchall()
    i = 1
    if (len(years) > 0):
        result += "Список фильмов по году: \n"
        for year in years:
            result += str(i) + ". " + year[1] + "\n"
            i = i + 1
    return (result)

def random_dorama():
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    quantity_of_id = cursor.execute("SELECT * FROM doramalist")
    quantity_of_id = cursor.fetchall()
    print(len(quantity_of_id))
    random_id = random.randint(1, len(quantity_of_id))
    print(random_id)
    cursor.execute("Select * from doramalist WHERE id = '" + str(random_id) + "'")
    dorama = cursor.fetchall()
    for title in dorama:
        result += cortege_parser(title)
    return (result)






connection = get_connection()
cursor = connection.cursor()


str4 = "Романтика , комедия"
str1 = "Абисс"
str2 = "Ю Ин На,Гон Ю"
str3 = "2016-2020"

print("Поиск по жанру")
result = genre_search(str4)
print(result)
print("Поиск по названию")
result = title_search(str1)
print(result)
print("Поиск по актерам")
result = actor_search(str2)
print(result)
print("Поиск по году")
result = year_search(str3)
print(result)
print("Случайная дорама")
result = random_dorama()
print(result)

#connection = get_connection()
#cursor = connection.cursor()
#quantity_of_id = cursor.execute("SELECT * FROM DoramasBD")
#quantity_of_id = cursor.fetchall()
#print(len(quantity_of_id))
#random_id = random.randint(1,len(quantity_of_id))
#print(random_id)

#add_to_favourites(12378,"Вы окружены")
