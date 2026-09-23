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

apps_ru = """
          ┌───────────────────────────┐
          │   ┌─────────────────────┐ │
          │   │ 1. Calcypython      │ │
          │   │ 2.Старый калькулятор│ │    
          │   │ 3. Игры             │ │
          │   │ 4. Календарь        │ │
          │   └─────────────────────┘ │
          └───────────────────────────┘
"""

import random
from config import language
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
       
    from config import name

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

    from config import name_ru 
    while not name_ru:
        print("Я думаю вы забыли ввести имя... Наверное?")
        from config import name_ru
    random_helloword = [
        "Привет, " + name_ru + "! Добро пожаловать в маленькую экосистему",
        "Ооо тут, " + name_ru + "! Проведём вместе время в экосистеме!",
        "Ооо Привет, " + name_ru + "! Желаю хорошего дня!"
    ]
    
    choice = random.choice(random_helloword)
    
    print(choice)
    
    print(apps_ru)
    
    choose = input("Выберите Приложения: ")
    while not choose:
        print("Выберите ПРИЛОЖЕНИЕ!!!!!!")
        choose = input("Выберите Приложения: ")
    if choose == "1" or choose == "Calcypython":
        import Calcypython  
    elif choose == "2" or choose == "Старый калькулятор":
        import Calcyold
    elif choose == "3" or choose == "Игры":
        import games
    elif choose == "4" or choose == "Календарь":
        import calendar
        from datetime import datetime
    
        print(calendar.calendar(datetime.now().year))   
        