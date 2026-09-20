welcome = """ 
          ┌──────────────────────┐
          │   ┌────────────────┐ │
          │   │ Welcome!  :)   │ │
          │   └────────────────┘ │
          └──────────────────────┘
        """

apps = """
          ┌───────────────────────────┐
          │   ┌─────────────────────┐ │
          │   │ 1. Calcypython      │ │
          │   │ 2. Old Calculator   │ │    
          │   │ 3. Games            │ │
          │   │ 4. Calendar         │ │
          │   └─────────────────────┘ │
          └───────────────────────────┘
          """

import random

language = input("Choice language (1.ru/2.en):")
while not language:
    print("Choice the language !!!!!!!!!!!!!!!!!")
    language = input("Choice language (1.ru/2.en):")

if language == "2.en" or language == "2" or language == "en":
    print("Ecosystem alpha starting...")

    print("welcome")
    print("My Github profile link : https://github.com/uzeroid666")
    from datetime import datetime
    time = datetime.now()
    print("Current date and time:", time)

    name = input("Please enter your name: ")
    while not name:
        print("I think you forgot to enter your name... Maybe?")
        name = input("Please enter your name: ")


    random_helloword = [
        "Hello, " + name + "! Welcome to Mini-Ecosystem!",
        "Hi there, " + name + "! Enjoy your time in the ecosystem!",
        "Greetings, " + name + "! Hope you have a great day!"
    ]

    choice = random.choice(random_helloword)

    print(choice)

    print(apps)

    choose = input("Choose an app: ")
    while not choose:
        print("Choice THE APP !!!!!!!!!")
        choose = input("Choose an app: ")
    if choose == "1" or choose == "Calcypython":
        import Calcypython  
    elif choose == "2" or choose == "Old Calculator":
        import Calcyold
    elif choose == "3" or choose == "Games":
        import games
    elif choose == "4" or  choose == "Calendar":
        import calendar
        from datetime import datetime

        print(calendar.calendar(datetime.now().year))
    import ecosystem

elif language == "1.ru" or language == "ru" or language == "1":
    print("Ecosystem alpha starting...")
    
    print("Добро пожаловать")
    print("ССылка на мой Github Профиль (там же выходят обновления) : https://github.com/uzeroid666")
    from datetime import datetime
    time = datetime.now()
    print("Нынешнее дата и время:", time)
    
    name = input("Пожалуйста введите своё имя: ")
    while not name:
        print("Я думаю вы забыли ввести имя... Наверное?")
        name = input("Пожалуйста введите своё имя: ")
    
    random_helloword = [
        "Привет, " + name + "! Добро пожаловать в маленькую экосистему",
        "Ооо тут, " + name + "! Проведём вместе время в экосистеме!",
        "Ооо Привет, " + name + "! Желаю хорошего дня!"
    ]
    
    choice = random.choice(random_helloword)
    
    print(choice)
    
    print(apps)
    
    choose = input("Выберите Приложения: ")
    while not choose:
        print("Выберите ПРИЛОЖЕНИЕ!!!!!!")
        choose = input("Выберите Приложения: ")
    if choose == "1" or choose == "Calcypython":
        import Calcypython  
    elif choose == "2" or choose == "Old Calculator":
        import Calcyold
    elif choose == "3" or choose == "Games":
        import games
    elif choose == "4" or choose == "Calendar":
        import calendar
        from datetime import datetime
    
        print(calendar.calendar(datetime.now().year))
    import ecosystem