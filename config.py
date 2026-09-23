language = input("Choice language (1.ru/2.en):")
if language == "2.en" or language == "2" or language == "en":
    name = input("Please enter your name: ")
    while not name:
        name = input("Enter your NAME: ")
elif language == "1.ru" or language == "ru" or language == "1":
    name_ru = input("Пожалуйста введите своё имя: ")
    while not name_ru:
        name_ru = input("введите своё ИМЯ: ")