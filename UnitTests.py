﻿import unittest
import telebot
import GeneralMessages
import DataBase


bot = telebot.TeleBot(token)

class TestMessageFirst(unittest.TestCase):
    def teststart(self):
        message = '\start'
        def handlestart(message):
            if (message == '\start'):
                bot.send_message(794135680,GeneralMessages.START_MSG)
                return(True)
        self.assertTrue(handlestart(message))
    def testhelp(self):
        message = '\help'
        def handlestart(message):
            if (message == '\help'):
                bot.send_message(794135680, GeneralMessages.HELP_MSG)
                return (True)

        self.assertTrue(handlestart(message))
    def testDB(self):
        str4 = "Романтика,комедия"
        str1 = "Абисс"
        str2 = "Ю Ин На"
        str3 = "2016-2020"
        self.assertEqual(DataBase.title_search(str1),'Название фильма: Абисс (Бездна / Abyss)\n'
'Год выпуска: 2019\n'
'Колличество эпизодов: 16\n'
'Жанры фильма: комедия, мистика, романтика, фантастика, детектив\n'
'Актеры в главных ролях: Ан Хё Соп, Пак Бо Ён, Пак Ми Хён, Пак Гон Рак, Ким О Бок, Пак Йе Ён, Ли Су Мин, Ким Са Ран\n'
'Описание фильма: Мистическо-романтическая дорама о волшебном шаре, способном перевоплощать души умерших в совершенно других людей. Чха Мин (Ан Хё Соп) – наследник ведущей корейской косметической компании.Хотя у него есть и ум, и богатство, он всегда был не уверен в своей внешности.Однако после того, как таинственный шар под названием «Бездна» попадает в его руки, он в итоге перевоплощается в потрясающе красивого администратора юридической фирмы.Чха Мин использует шар для реинкарнации Го Се Ён (Пак Бо Ён), жесткой, опытной и красивой женщины-прокурора, которая была убита в своей квартире.После того, как она таинственно вернулась к жизни в качестве адвоката в юридической фирме с совершенно новым, но заурядным лицом, она намерена раскрыть тайну своего перевоплощения.\n'
'Рейтинг фильма: 7.1\n'
'Ссылка на фильм: https://doramatv.live/abyss\n'
'\n')
        self.assertEqual(DataBase.actor_search(str2),'Название фильма: Токкэби (Гоблин / Демон)\n'
'Год выпуска: 2017\n'
'Колличество эпизодов: 16\n'
'Жанры фильма: драма, фэнтези, исторический, мистика, романтика, дружба\n'
'Актеры в главных ролях: Ю Ин На, Гон Ю, Ким Го Ын, Юк Сон Чжэ, Ли Дон Ук, Чо Ин У, Соль У Хён, Пак Се Ван, Ан Джи Хён, Ли Мун Су, Ким Со Ра\n'
'Описание фильма: Бессмертный демон токкэби много лет живет среди смертных и порядком устал от жизни.Но если ты волшебное существо, есть лишь один способ поставить точку и покинуть бренный мир - жениться на смертной.Избранницей демона становится девушка, которая может видеть призраков.А жнец смерти, чья задача провожать души умерших в загробный мир, тем временем потерял память.\n'
'Рейтинг фильма: 8.6\n'
'Ссылка на фильм: https://doramatv.live/goblin\n'
'\n')
        self.assertEqual(DataBase.year_search(str3),'Список фильмов по году: \n' 
'1. Аварийная посадка любви\n'
'2. Итэвон класс\n'
'3. Токкэби (Гоблин / Демон)\n'
'4. Мудрая жизнь в больнице (Hospital Playlist)\n'
'5. Абисс (Бездна / Abyss)\n'
'6. Радио "Романтика"\n'
'7. Силачка До Бон Сун\n'
'8. Отель Дель Луна\n'
'9. W: Меж двух миров\n'
'10. Круглосуточный магазин Сэт Бёль (Backstreet Rookie)\n')
        self.assertEqual(DataBase.genre_search(str4),'Список фильмов по жанру: \n' 
'1. Аварийная посадка любви\n'
'2. Мудрая жизнь в больнице (Hospital Playlist)\n'
'3. Абисс (Бездна / Abyss)\n'
'4. Радио "Романтика"\n'
'5. Силачка До Бон Сун\n'
'6. Круглосуточный магазин Сэт Бёль (Backstreet Rookie)\n')

