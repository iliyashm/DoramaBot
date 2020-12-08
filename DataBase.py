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
    parser = message.split(",")
    command = "Select * FROM doramalist WHERE genre LIKE '%" + parser[0] + "%' "
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
    result += "Список фильмов по жанру: \n"
    for genre in genres:
        #result += cortege_parser(genre)
        #cortege = list(genre)
        result += str(i) + ". " + genre[1] + "\n"
        i = i + 1
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
    command = "Select * FROM doramalist WHERE name_of_movie LIKE '%" + str + "%' "
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
    list = str1.split("-")
    if len(list) == 1:
        command = "Select * FROM doramalist WHERE year = " + list[i]
    if len(list) > 1:
        if list[0] < list[1]:
            command = "Select * FROM doramalist WHERE year >= '" + list[i] + "' AND year <= '" + list[i+1] + "'"
    cursor.execute(command)
    years = cursor.fetchall()
    i = 1
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



#inser_into_table("users",10,"JK","ROLLING")

#sql = "insert into doramalist(name_of_movie, year, number_of_episodes, genre, actors, description, rating_of_movie, link) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#val = [
    #('Аварийная посадка любви',2020,16,'комедия, романтика, драма','Хён Бин, Сон Йе Чжин, Ким Джон Хён, Со Джи Хе, Чхве Чжи У, Пан Ын Чжин, Ли Хо Чжон, Хон У Джин, Сон Чон Хва, Ю Су Бин','Юн Се Ри (Сон Йе Чжин) - наследница конгломерата в Южной Корее. Однажды на занятиях парапланеризма с ней происходит несчастный случай: торнадо заставляет совершить аварийную посадку в Северной Корее.Там она встречает Ри Чон Хёка (Хён Бин), офицера северокорейской армии.Чон Хёку ничего не остаётся кроме как укрывать её от начальства, ведь его подчинённым придётся не сладко, если все узнают, что шпионка с юга пересекла демилитаризованную зону во время дежурства отряда.Вскоре главные герои влюбляются друг в друга. Удастся ли капитану Ри Чон Хёку спасти и защитить Се Ри?',8.7,'https://doramatv.live/avariinaia_posadka_liubvi'),
    #('Итэвон класс'
	#,2020
	#,16
	#,'повседневность, бизнес, драма, дружба, романтика'
	#,'Ю Джэ Мён, Квон На Ра, Пак Со Джун, Ким Да Ми, Хван Ин Джун, Ким Ик Тхэ, Сон Хён Чжу, Хон Сок Чхон, Ким Джи Ён, Ким Хе Ын'
	#,'История бывшего осужденного Пак Сэрои (Пак Соджун), чья жизнь перевернулась с ног на голову после того, как его исключили из школы.Он потерял отца из-за хулигана-одноклассника Чан Гынвона (Ан Бохён), сына генерального директора крупной корпорации, Чан Дэхи (Ю Джэмён).Пак Сэрои открывает свой бар-ресторан Данбан в Итхэвоне и вместе со своим менеджером Чо Исо (Ким Дами) и сотрудниками стремится к достижению больших высот.'
	#,8.2
	#,'https://doramatv.live/ithevon_klass'),
    #('Токкэби (Гоблин / Демон)'
	#,2017
	#,16
	#,'драма, фэнтези, исторический, мистика, романтика, дружба'
	#,'Ю Ин На, Гон Ю, Ким Го Ын, Юк Сон Чжэ, Ли Дон Ук, Чо Ин У, Соль У Хён, Пак Се Ван, Ан Джи Хён, Ли Мун Су, Ким Со Ра'
	#,'Бессмертный демон токкэби много лет живет среди смертных и порядком устал от жизни.Но если ты волшебное существо, есть лишь один способ поставить точку и покинуть бренный мир - жениться на смертной.Избранницей демона становится девушка, которая может видеть призраков.А жнец смерти, чья задача провожать души умерших в загробный мир, тем временем потерял память.'
	#,8.6
	#,'https://doramatv.live/goblin'),
    #('Мудрая жизнь в больнице (Hospital Playlist)'
	#,2020
	#,12
	#,'повседневность, комедия, дружба, медицина, романтика, драма'
	#,'Чон Кён Хо, Ю Ён Сок, Ким Дэ Мён, Чо Джон Сок, Чон Ми До, Чхве Ён Дон, Пэ Хён Сон, Ким Хе Ин, Чон Мун Сон, Ан Ын Джин, Мун Хи Гён'
	#,'Основная тема дорамы — гуманизм.Сериал рассказывает о том, как работает больница, о трудностях, с которыми сталкиваются врачи, медсёстры, пациенты и другие.'
	#,8.7
	#,'https://doramatv.live/mudraia_jizn_v_bolnice'),
    #('Абисс (Бездна / Abyss)'
	#,2019
	#,16
	#,'комедия, мистика, романтика, фантастика, детектив'
	#,'Ан Хё Соп, Пак Бо Ён, Пак Ми Хён, Пак Гон Рак, Ким О Бок, Пак Йе Ён, Ли Су Мин, Ким Са Ран'
	#,'Мистическо-романтическая дорама о волшебном шаре, способном перевоплощать души умерших в совершенно других людей. Чха Мин (Ан Хё Соп) – наследник ведущей корейской косметической компании.Хотя у него есть и ум, и богатство, он всегда был не уверен в своей внешности.Однако после того, как таинственный шар под названием «Бездна» попадает в его руки, он в итоге перевоплощается в потрясающе красивого администратора юридической фирмы.Чха Мин использует шар для реинкарнации Го Се Ён (Пак Бо Ён), жесткой, опытной и красивой женщины-прокурора, которая была убита в своей квартире.После того, как она таинственно вернулась к жизни в качестве адвоката в юридической фирме с совершенно новым, но заурядным лицом, она намерена раскрыть тайну своего перевоплощения.'
	#,7.1
	#,'https://doramatv.live/abyss'),
    #('Радио "Романтика"'
	#,2018
	#,16
	#,'романтика, комедия, мелодрама'
	#,'Юн Ду Джун, Ким Со Хён, Ю Ра, Ли Ый Ун, Ким Хе Ын, Ким Бён Се, Ким Ю Квон, Квак Дон Ён'
	#,'Сон Гы Рим (Ким Со Хён) работает редактором радиопрограмм.В детстве она часто слушала радио со своей слепой матерью.Именно это вдохновило девушку стать редактором, но пока ей не удается проявить свой талант в полной мере.Программа, над которой работает Сон Гы Рим, находится на грани закрытия.Однако героине удается привлечь к участию популярного актера Чи Су Хо (Юн Ду Джун).'
	#,6.6
	#,'https://doramatv.live/radio_romance'),
    #('Силачка До Бон Сун'
	#,2017
	#,16
	#,'фантастика, детектив, романтика, комедия'
	#,'Джи Су, Пак Хён Сик, Пак Бо Ён, Ли Сан, Ким Вон Хэ, Им Вон Хи, Чхве Ён Шин, Чан Ми Кван, Юн Сан Хён'
	#,'До Бон Сун (Пак Бо Ён) с рождения наделена сверхчеловеческой физической силой.Если она не будет осторожна, то с легкостью сломает то, к чему прикасается.К тому же она давно влюблена в Гук Ду (Джи Су), который обожает придерживаться установленных правил.Девушка отчаянно хочет походить на его идеальный тип – милую и изящную леди.Благодаря своей физической силе Бон Сун получает работу в качестве телохранителя избалованного богача Ан Мин Хёка (Пак Хён Сик), который является директором компании, занимающейся созданием видеоигр.В отличие от Гук Ду, Мин Хёк – высокомерный чудик, пренебрегающий всякими правилами.'
	#,8.2
	#,'https://doramatv.live/strong_woman_do_bong_soon'),
    #('Отель Дель Луна'
	#,2019
	#,16
	#,'драма, романтика, фэнтези, мелодрама, мистика'
	#,'Ё Чжин Гу, АйЮ, Ким Вон Хэ, Ким О Бок, Чан Чжу Ён, Чхве Ю Сон, Солли, Ким Гю Ри'
	#,'Неожиданный случай приводит к тому, что главный герой Ко Чхан Сон (Ё Чжин Гу) начинает работать управляющим в таинственном отеле "Hotel del Luna", где по коридорам бродят призраки.Владеет отелем Чжан Ман Воль (АйЮ).Она красива, но довольна холодна с людьми.Кроме этого, из-за ошибки прошлого она уже 1000 лет находится под проклятием.'
	#,8.3
	#,'https://doramatv.live/otel_del_luna'),
    #('W: Меж двух миров'
	#,2016
	#,16
	#,'романтика, фантастика, триллер'
	#,'Ли Чон Сок, Хан Хё Чжу, Пак Гон Рак, Пак Вон Сан, Ким Ик Тхэ, Ли Юн Сан, Ким Кван Хён, Ли Тэ Хван'
	#,'Фантастическая история про женщину-хирурга Ён Джу и предпринимателя-авантюриста Кан Чоля, главного героя популярного веб-комикса, автором которого является отец Ён Джу.Несмотря на то, что они живут в наше время в Сеуле, они как бы находятся в разных мирах.События переплетаются между реальностью и иллюзией. И в какой-то момент судьбы героев пересекаются. '
	#,8.1
	#,'https://doramatv.live/w___two_worlds'),
    #('Круглосуточный магазин Сэт Бёль (Backstreet Rookie)'
	#,2020
	#,16
	#,'романтика, комедия'
	#,'Ким Ю Чжон, Чжи Чан Ук, Чон Ын Джи, Юн Сыль, Ли Джун Ён, Рю Сын Су, Ли Юн Хви, Гам Со Хён'
	#,'Дорама рассказывает о красивом, но неуклюжем менеджере в круглосуточном магазине по имени Чхве Дэ Хён (Чжи Чан Ук) и изворотливой и озорной работнице на полставки Чон Сэт Бёль (Ким Ю Чжон).Чхве Дэ Хён в юном возрасте оставил работу в крупной компании и открыл собственный круглосуточный магазин.К нему устраивается остроумная Чон Сэт Бёль, желающая оставить прошлое позади и начать жить заново в качестве молодой женщины, ищущей справедливость.'
	#,7.4
	#,'https://doramatv.live/kruglosutochnyi_magazin_set_bel'),
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

str4 = "Романтика,комедия"
str1 = "Абисс"
str2 = "Ю Ин На"
str3 = "2016-2020"
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