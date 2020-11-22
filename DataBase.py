# -*- coding: utf-8 -*-
import mysql.connector
import random


def get_connection():
    connection = mysql.connector.connect(
        host = "127.7.7.1",
        user = "root",
        password = "12345",
        database = "doramadb"
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

    cursor.execute("CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY,id_user INT, name_of_movie VARCHAR(255))".format(table_name))
    cursor.execute("SHOW TABLES")

    for tb in cursor:
        print(tb)

#add_table_in_database("Favourites")


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
            "Актеры в главных ролях: " + cortege[3] + "\n" \
            "Описание фильма: " + cortege[4] + "\n" \
            "Рейтинг фильма: " + str(cortege[5]) + "\n" \
            "Жанры фильма: " +  cortege[6] + "\n" \
            "\n"
    return (result)

def add_to_favourites(user_id,str1):
    connection = get_connection()
    cursor = connection.cursor()
    command = "Select title FROM DoramasBD WHERE title LIKE '%" + str1 + "%' "
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
    parser = message.split(",")
    command = "Select * FROM DoramasBD WHERE genres LIKE '%" + parser[0] + "%' "
    if len(parser) > 1:
        for genre in parser:
            if i == 0:
                i = i + 1
                continue
            command += "AND genres LIKE '%" + parser[i] + "%'"
            i = i + 1
    cursor.execute(command)
    genres = cursor.fetchall()
    for genre in genres:
        result += cortege_parser(genre)
        #cortege = list(genre)
        #result += "Название фильма: " + cortege[1] + "\n" \
        #"Год выпуска: " + str(cortege[2]) + "\n" \
        #"Актеры в главных ролях: " + cortege[3] + "\n" \
        #"Описание фильма: " + cortege[4] + "\n" \
        #"Рейтинг фильма: " + str(cortege[5]) + "\n" \
        #"Жанры фильма: " + cortege[6] + "\n" \
        #"\n"
    return (result)

def title_search(str):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    command = "Select * FROM DoramasBD WHERE title LIKE '%" + str + "%' "
    cursor.execute(command)
    titles = cursor.fetchall()
    for title in titles:
        result += cortege_parser(title)
    #parse = title.split(",")
    #return (parse)
    return(result)

def actor_search(str):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    i = 0
    list = []
    list = str.split(",")
    command = "Select * FROM DoramasBD WHERE actors LIKE '%" + list[0] + "%' "
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

def year_search(str):
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    i = 0
    list = []
    list = str.split("-")
    if len(list) == 1:
        command = "Select * FROM DoramasBD WHERE year = " + list[i]
    if len(list) > 1:
        if list[0] > list[1]:
            command = "Select * FROM DoramasBD WHERE year >= '" + list[i] + "' AND year <= '" + list[i+1] + "'"
    cursor.execute(command)
    years = cursor.fetchall()
    for year in years:
        result += cortege_parser(year)
    return (result)

def random_dorama():
    connection = get_connection()
    cursor = connection.cursor()
    result = ''
    quantity_of_id = cursor.execute("SELECT * FROM DoramasBD")
    quantity_of_id = cursor.fetchall()
    print(len(quantity_of_id))
    random_id = random.randint(1, len(quantity_of_id))
    print(random_id)
    cursor.execute("Select * from DoramasBD WHERE id_dorama = '" + str(random_id) + "'")
    dorama = cursor.fetchall()
    for title in dorama:
        result += cortege_parser(title)
    return (result)



#inser_into_table("users",10,"JK","ROLLING")

#sql = "INSERT INTO DoramasBD (title,year,actors,description,rating_of_movie,genres) VALUES(%s,%s,%s,%s,%s,%s)"
#val = [
    #("Бегущий человек", "2010","Ли Кван Су,Сон Джи Хё,Сон Джун Ки,Чон Со Мин,Ян Се Чан","Бегущий человек – это корейское телешоу; часть блока Good Sunday на канале SBS. Премьера состоялась 11 июля 2010, на данный момент самая долгоиграющая программа на канале SBS. Шоу снято в жанре «погоня», жанр разных шоу в городской среде. Ведущие и гости участвуют в миссиях на выживание чтобы выиграть гонку.","5","Шоу,комедия"),
    #("Любовь со временем","2020","Чжао Чэн Юй, Жэнь Янь Кай, Чэн Сяо Мэн, Ли Цзюнь Фэн, Лю Юй Ци","Они ненавидели друг друга ещё со школы. Но судьба распорядилась так, что эти двое женились по расчёту. Она – неизвестный писатель, чья семья находится в затруднительном положении. Он – гуру инвестиций. Они совершенно разные, но вынуждены жить вместе как женатая пара. Получится ли у них?","4","Романтика,повседневность"),
    #("Вы окружены", "2014","Ан Джэ Хён, Чха Сын Вон, Ли Сын Ги, Го А Ра, Пак Чон Мин","Полицейский участок Каннама в Сеуле переводится в аварийный режим: легендарному детективу Со Пан Соку и капитану Ли выдали в подчинение четырех новобранцев. Неуклюжий Джи Гук пошел в детективы, потому что не попал в патрульную службу, красавчик Пак Тэ Иль оказался здесь, потому что детективом быть весело, О Су Сон, единственная девушка в команде, пришла ради стабильной заработной платы, а мрачный Ын Дэ Гу слишком неразговорчив, чтобы понять, что у него на уме. Берегитесь, «детишки», потому что за небрежное отношение к работе детектива руководитель Со с вас три шкуры снимет!","4","криминал, детектив, комедия, романтика, драма"),
#]
#connection = get_connection()
#cursor = connection.cursor()
#cursor.executemany(sql,val)
#connection.commit()

connection = get_connection()
cursor = connection.cursor()
#genre1 = 'Романтика'
#genre2 = 'приключения'
#cursor.execute("Select * FROM DoramasBD WHERE genres LIKE '%" + genre1 + "%' AND genres LIKE '%"+ genre2+ "%' ")
#genres = cursor.fetchall()

#for genre in genres:
    #print(genre)

str4 = "Романтика"
str1 = "Любовь"
str2 = "Чжао Чэн Юй"
str3 = "2020"
#print (str.split(","))
#list = []
#list = str.split(",")
#print(list)
#print(len(list))
#i = 0
#command = "Select * FROM DoramasBD WHERE genres LIKE '%" + list[0] + "%' "

#if len(list) > 1:
    #for genres in list :
        #if i == 0:
            #i = i + 1
            #continue
        #command += "AND genres LIKE '%" + list[i] + "%'"
        #i = i + 1
#else:
    #cursor.execute(command)
    #genres = cursor.fetchall()
    #for genre in genres:
        #print(genre)

#cursor.execute(command)
#genres = cursor.fetchall()
#for genre in genres:
    #print(genre)
print("Поиск по жанру")
result = genre_search(str4)
print(result)
print("Поиск по названию")
title_search(str1)
print("Поиск по актерам")
actor_search(str2)
print("Поиск по году")
year_search(str3)
print("Случайная дорама")
random_dorama()

#connection = get_connection()
#cursor = connection.cursor()
#quantity_of_id = cursor.execute("SELECT * FROM DoramasBD")
#quantity_of_id = cursor.fetchall()
#print(len(quantity_of_id))
#random_id = random.randint(1,len(quantity_of_id))
#print(random_id)

#add_to_favourites(12378,"Вы окружены")