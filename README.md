# DoramalistBot для Telegram  
Бот, предназначенный для поиска дорам из базы данных по разным критериям, также реализующий работу со списком избранного.
# Состав команды
*(Все из группы 3530202/80201):*
- Ладвищенко Ирина
- Останина Анна
- Шмелёв Илья
# Введение и определение проблемы
Задачей курса является сделать проект и пройти большинство классических стадий создания ПО, в меньше степени опираясь на тему курсовой работы, а на работоспособность и оформление. Мы решили сделать аналог ресурса myanimelist с японской анимацией, но для корейских сериалов. Прямых известных аналогов не найдено, поэтому проект может быть актуален для поклонников данной сферы.

Основная задача - адаптировать в Telegram англоязычный doramalist для русскоговорящих пользователей, опираясь на русскоязычные сайты с корейскими сериалами (Кинопоиск, dorama.tv и другие).
# Выработка требований
В начале работы были выработаны пользовательские истории, на основе которых формировались дальнейшие требования к программе. Ниже приведены основные их них.

Технические (нефункциональные) требования к системе и функциональные требования к продукту:

-   Корректная работа внешних ресурсов: БД с данными о дорамах, библиотеки telebot и pyTelegramBotAPI для Python, сервера Telegram для реализации обмена сообщениями (требуется надежное Интернет-соединение)
    
-   UI продукта: использован интерфейс приложения Telegram; взаимодействие с пользователем происходит посредством обмена сообщениями в персональном чате с ботом, для выбора команд через \ также реализуются кнопки
    
-   Реализация функций бота:  
    - \start (начало работы: бот поприветствует вас и предложит ознакомиться с его функциями)  
    - \help (вызов справки о функциях бота: бот выдаст список всех своих функций с описаниями)  
    - ‘поиск по жанру’ (бот предложит ввести жанры, а затем выдаст подходящие дорамы)  
    - ‘поиск по названию’ (бот предложит ввести название дорамы, а затем выдаст информацию о ней)  
    - ‘поиск по актеру’ (бот предложит ввести имена актеров, а затем выдаст дорамы, в которых они играют)  
    - ‘поиск по году выпуска’ (бот предложит ввести интересующий диапазон лет, а затем выдаст подходящие дорамы)  
    - работа с “Избранным” (‘Избранное’/’Добавить в избранное’/’Удалить из избранного’ - пользователь вводит название, бот обрабатывает и работает с персональным списком пользователя aka “К просмотру”)  
    - случайная дорама (бот выведет информацию о случайной дораме из базы)
    
-   Обработка запросов, не входящих в рамки функций бота: бот должен обрабатывать любое сообщение пользователя - если введенный текст не соответствует ни одной из команд бота, он сообщит об этом пользователю
# Разработка архитектуры и детальное проектирование
На данном этапе реализованы первые две диаграммы из подхода The C4 model for visualizing software architecture ([https://c4model.com/](https://c4model.com/)).

**1.  System context diagram**
Данная диаграмма показывает проект, над которым мы работаем, другие системы вокруг проекта, с которыми проект может контактировать, и людей, которые используют продукт.
**![](https://lh3.googleusercontent.com/QWsMTdWiZFoUKudLw3kagQetUcEEN6pFxCbIV8cYOOjh9wLzK2yd5SUte0RtOFNFYLsseasQHBobRIp6DgpylBfGKYrOGnPiH2yZhGrAXDIDLKQ-3_lRFUDA6mQMrzinswLVL3g)**

**2.  Container diagram**
Что находится внутри телеграм-бота и какие технологии используются позволяет узнать Container diagram. Диаграмма показывает все ваши приложения, базы данных, и как они связаны.
**![](https://lh3.googleusercontent.com/bwL6npjtM-P0AtnaajHFTwK7xOYogLEJt6QThqC3BwG5yCxLIXMrq7EiRHXXIF1Dmo6SHLlO5gbstZYofLuPq9nDpVGzs2GDBMRyRNeqOp_HJFoF88g4sli5FRoUUVbO6BDOULw)**
# Кодирование и отладка
Разработка велась на языке Python версии 3.7 в среде PyCharm 2020.1 с использованием базы данных MySQL и библиотек telebot и pyTelegramBotAPI.
Во время кодирования был разработан класс работы с базой данных MySQL(функции для получения тех или иных данных по запросам), проверены функции БД через юнит тесты, и написан сам основной функционал пошагового бота в файле main. Трудности возникали только на этапе установки библиотек, так как среда разработки отказывалась их видеть(в локальной сборке указано как решить самую часто встречающуюся проблему).
# Unit-тестирование и интеграционное тестирование
Разработанные Unit-тесты (см. файл UnitTests.py) покрывают стартовые команды бота (\) и запросы к базе данных. Т.к. охватить непосредственно текстовые команды бота обычным подходом к Unit-тестированию не удалось (т.к. возникли сложности с получением данных с сервера из-за использования UI Telegram и реализации бота непосредственно в чате), а подходящих утилит для написания Unit-тестов для Telegram-ботов найти не удалось, то тестирование было произведено вручную в соответствии с требованиями к системе, описанными выше. Интеграционное тестирование было проведено также вручную по восходящей стратегии (работа отдельных функций тестировалась независимо на этапе разработки). Наглядные примеры можно увидеть ниже:
1. Начало работы
**![](https://lh6.googleusercontent.com/aBpYtt_4I3CkzBwxrdEC7J-iuByv1R8gEXW1XtNylGfcYfpWZGW4JW-fkyCoLcDP1CKuKTMIw7HGkkg2C31atn544fFmmVnmck8KJHML_UwV5vMe9y-Cc1j4XcPdzQ)**
2. Кнопки и список функций
**![](https://lh4.googleusercontent.com/5YM2_3BYg6TezjENgP8OS6Q8dBgPj0c5bt-V8kuqdAHEOFP-O4sfvMx7KUTw1tWrl9bFPhr_yNLfJZ60Jv2S2c0wPzf4GzTvM4Wrr57v1vNrhvhYxCyZ1Mx8WjmVbA)**
**![](https://lh4.googleusercontent.com/Msmy0-xopZSy703LvoDmP2OEsMMKetNy2RARNWrOCZG-zHbdAy2CUmrQEFH81_dQvJoIDe33YVK11jxOv8XPj-3OMVpkWKrGrCptKETbAPveW_sd-OTxIJgVzn84Eg)**
3. Поиск по жанру
**![](https://lh3.googleusercontent.com/zPEXJdvweDIp6iXiwaF_yOvla_wfXeJ1l2S1sfFWv0nm22qpX_k_SKV_B3kNacUYlI13NpYl0wzu-zFhn8Id844n7ljCYdas8nVoH1FbjS0CyMhC3128DgKC262ldA)**
**![](https://lh3.googleusercontent.com/ORmrhim3BlOTwuhLJwFnMQGfO-UF1Amd2jJrAb6jLg6beyoSHfcl1aYs2t6QVN-fPEnRMF6GEkT8RpVKRlhAW1qDTpYhCEeLHhzj4RllxVRx0H6sQaiJ3UZBjyIO6w)**
4. Поиск по названию
**![](https://lh4.googleusercontent.com/X2xy4mmiPQwh7qip5pVqXlF_g1FK9QSoiF37L6kF4YGor8PNnAkbJDZZ56JYeN3sT2RufrS0tVrjQ6vV6MKCcDjUqinD3x1anIWvE-awYRHQ1hYFW8uA1-np7TNgaQ)**
**![](https://lh3.googleusercontent.com/onVwFVyGfF-T_aTyotyYCk2p__Ht2YSyMmen65rxqhGguN-zeVP3mJY9LH9UG_DS0nK_flFFSmy5B3XJM6P_OHZwpczX0NrD3R9_Jb5ZxE1gRBAn7zsbpwbz27BMKA)**
5. Поиск по актеру
**![](https://lh4.googleusercontent.com/bN7ivd6j8oHF959VXwuYAZ6pHnhhLYF76K0VSDcSoZTPR9A-pyFfc0R2FPBDCRP164JnGtyJkBxA_5W6sH4EmUOYGnf5s-_WQXsPBPUJAS9Hc8uhZPR4o4age9mOoQ)**
**![](https://lh3.googleusercontent.com/SSZejSm6SHwwZDt-1SVBgqaUn8FPQzb11x5xk27jncEwfVPlmiQKXQSiSki3uw1PAoWfndtPKfWdZomWuJeuiXt6PQbKoL3eOmmfUa_80QAsT_dMaSVJ2QsUCw72Xg)**
6. Поиск по году
**![](https://lh5.googleusercontent.com/OR7G2hNett_eUetaXQ-hbKWD_tAfopwripYXTF_C2RsdDSHmjkJ8cn1yjXSqPpBY1JYhl84IMhaZF0zo4hl7FLJ3i0toXNLryfp-gH_4GC_2Jq6Hl8twFlahHwju1g)**
**![](https://lh5.googleusercontent.com/hspML3yZcbhQi4mENqHcGKSEg895XLuFtxHmildpAGB_e96tcWLpoBWdg6wbK_VqJ1n80Ww2KJ3LJ5L4vKVk0_dIZczvxfj5O99RNmW_r1W4-4YSesTBib_Lxp_Smg)**
7. Добавить в избранное
**![](https://lh6.googleusercontent.com/dPSJpXFS60cjlrtAPrSy7Dbbh9eZO1ygpkIUJp5Y0uNJCogNJeZErnSpGClx9aryXvp2tV9ig8hEjnYqg8sQG5FEMwrQncoDdeZtWj5mVETJ25eqeGfM7ajSveiWbg)**
**![](https://lh6.googleusercontent.com/FzXMztciCunoU1Tb7WMOup-geiYCyRNTPF8xJh_vwQcWQyvFfzjjqmeUpT2X7Gkz_UHzeIgPEaYxLwWo54V-TmTdVbgAIknzuAZ6RvMFsGB0COrrBYTQv7pujdiMpA)**
**![](https://lh5.googleusercontent.com/5NV6dCYLe-IfeIJogN11jjYbrXrsuVCuq812ZiIbnQjkTczIs9_ITeeaTo9PWRREwrSSwD4B6VO-y6ozC74QIG15H7I0Vq4XkVsj2EiOkVWaxafTdeFp_1BSoFuZxA)**
8. Избранное
**![](https://lh5.googleusercontent.com/gqSCvkV0nUs9jBM694GyspmEfW6_lx5DJOaY6pjw1RAAm20wkQU-kEGr6Mw7_ZJv9lg1JAYB7hbgV4gmCHc9jBUFq8btO8RtIooenmQFiOCyQP2UGu4WvVQtO76W4Q)**
9. Удалить из избранного
**![](https://lh6.googleusercontent.com/CpFzf6E-8yzuJ5267yQT9bWHOFdBjraGOJ_-Ni_Pi63uSA99bigmSfA3B1iYPkIAQbvbDsp_VWceaQU9Mn9dEC07wnzPSm1PDCgAaf9RnSx14cPPl4E5puMvO8SEsw)**
**![](https://lh4.googleusercontent.com/DUxT4jaQFrjP78LI7Z0xQEN8RL-f2IzTpGVcPU6-rl_hPxpp9om3Ao8wVuqkAFqNqkjHx3S7Nf-3wx78gkvhMcDw-9uRtCPcTlo9VydK1mP-hyxM3JN7VzStJOsNDw)**
10. Случайная дорама
**![](https://lh3.googleusercontent.com/JM7ZA4lJbsjndT_-AvdYB8_LHe6mL3mHt06Qzgwlw2eJBt1tfe0ruVfhLSWSUxOmvEZhMo4p9I8Caqryg3y-aZF7VRkOgCDubUiVZmV8SSRG5xznwAep4Ynr8MV31w)**
11. Обработка нераспознанных команд
**![](https://lh4.googleusercontent.com/9h0o74X3boOV2RQU4HmBNtPssOEOTJqRW5guJH9pidBU1qpgvl6jrKiVb9yeTs0268rlhHo3kf25sDIFKyZ1GKvr1PnCTyrQKziy6U3eVsvR8CrQao_nKPdD87Fmog)**

## Локальная сборка
Для того, чтобы собрать бота на своем устройстве:
1.  Скопируйте все файлы в свой проект
2.  Загрузите библиотеки mysql-connector, mysql-connector-python, telebot и pyTelegramBotAPI через pip install (или через Settings -> Python Interpreter, если у вас установлен PyCharm)

*Адрес бота в Telegram:* @DoramalistBot

*Примечание*: если при запуске возникает ошибка с отсутствием message-handler, удалите библиотеки telebot и pyTelegramBotAPI, затем снова установите ТОЛЬКО pyTelegramBotAPI свежей версии. После этого перезапустите проект.
# Результаты работы

В рамках дисциплины был реализован телеграм-бот, с которым были пройдены классические стадии создания ПО, такие как: собрана команда для реализации проекта, была определена проблема, выработаны требования, разработана архитектура, написана и отлажена программа, проведено тестирование. Данный телеграм-бот для корейских дорам doramalist является аналогом для русскоязычных пользователей англоязычного ресурса myanimelist, который работает с японской анимацией. В дальнейшем бота возможно применить и для более широкого спектра фильмов и сериалов. Точками расширения являются непосредственно БД с дорамами, функции личного оценивания просмотренных дорам пользователями, а также установка различных статусов для дорам из “Избранного” (смотрю, бросил и др.).



