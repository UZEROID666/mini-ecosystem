games = """
                  ┌───────────────────────────┐
                  │   ┌─────────────────────┐ │
                  │   │ 1. Slot machine     │ │
                  │   │ 2. P.S.R            │ │
                  │   │ 3.Guess the number  │ │
                  │   └─────────────────────┘ │
                  └───────────────────────────┘
"""

games_ru = """
                  ┌───────────────────────────┐
                  │   ┌─────────────────────┐ │
                  │   │ 1. Слот машина      │ │
                  │   │ 2. К.Н.Б            │ │
                  │   │ 3.Угадай число      │ │
                  │   └─────────────────────┘ │
                  └───────────────────────────┘
"""

import random
from ecosystem import name, language 
if language == "2.en" or language == "2" or language == "en":
    print(f"{name} welcome")
    print(games)
    gc = input("Choice the game: ")
    if gc == "1" or gc == "Slot machine":
        while True:
            print("""
            ┌───────────────────────┐
            │     SLOT MACHINE      │
            │                       │
            │  1. Spin 🎰           │
            │  2. Exit              │
            └───────────────────────┘
            """)

            choice = input("Choose: ")

            if choice == "2":
                print("Exiting Slot Machine...")
                break

            elif choice == "1":
                choicer = ("7", "🍒", "💀", "🏆")

                slot1 = random.choice(choicer)
                slot2 = random.choice(choicer)
                slot3 = random.choice(choicer)

                print(slot1, slot2, slot3)

                if slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("WOOOOW, YOU X3 WIN JACKPOT!!!")

                elif slot1 == "🍒" and slot2 == "🍒" and slot3 == "🍒":
                    print("My Congratulations, You WIN Jackpot")

                elif slot1 == "🏆" and slot2 == "🏆" and slot3 == "🏆":
                    print("My Congratulations, You WIN X2 JACKPOT")

                elif slot1 == "💀" and slot2 == "💀" and slot3 == "💀":
                    print("You will die. Of Course I am Joking or not?")

                else:
                    print("You lose your chance")

            else:
                print("Invalid choice!")
            
    elif gc == "2" or gc == "P.S.R":
        while True:
            psr = "rock" , "paper" , "scissors"
            choicer = random.choice(psr)
            player = input("Rock, Paper or scissors?: ")
            if choicer == "rock" and player == "rock":
                print(choicer)
                print("It's a draw")
            elif choicer == "rock" and player == "scissors":
                print(choicer)
                print("You lost :(")
            elif choicer == "rock" and player == "paper":
                print(choicer)
                print("You win!")
            elif choicer == "paper" and player == "paper":
                print(choicer)
                print("It's a draw")
            elif choicer == "paper" and player == "scissors":
                print(choicer)
                print("You win!")
            elif choicer == "paper" and player == "rock":
                print(choicer)
                print("You lost :(")
            elif choicer == "scissors" and player == "scissors":
                print(choicer)
                print("It's a draw")
            elif choicer == "scissors" and player == "paper":
                print(choicer)
                print("You lost :(")
            elif choicer == "scissors" and player == "rock":
                print(choicer)
                print("You win!")
            else:
                print("Wrong word❌")
    elif gc == "3" or gc == "Guess the number":
        while True:
            rn = random.randint(1, 1000)
            pn = int(input("Guess the number (1 , 1000): "))
            if rn == pn:
                print(f"My number is {rn}")
                print("Wow , You Win!")
            else:
                print(f"Sorry but my number is {rn}")
    else:
        print("Invalid Choose ❌")
        import games

elif language == "1.ru" or language == "ru" or language == "1":
    print(f"{name} Уэлком")
    print(games_ru)
    gc = input("Выберите игру: ")
    if gc == "1" or gc == "Слот машина":
        while True:
            print("""
            ┌───────────────────────┐
            │     SLOT MACHINE      │
            │                       │
            │  1. Крутить🎰         │
            │  2. Выйти             │
            └───────────────────────┘
            """)

            choice = input("Выбери: ")

            if choice == "2":
                print("ВЫдходим из слот машины...")
                break

            elif choice == "1":
                choicer = ("7", "🍒", "💀", "🏆")

                slot1 = random.choice(choicer)
                slot2 = random.choice(choicer)
                slot3 = random.choice(choicer)

                print(slot1, slot2, slot3)

                if slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("ВООООУ, ТЫ ВЫИГРАЛ Х3 ДЖЕКПОТ!!!")

                elif slot1 == "🍒" and slot2 == "🍒" and slot3 == "🍒":
                    print("Мои поздравления, Ты ВЫИГРАЛ Джекпот")

                elif slot1 == "🏆" and slot2 == "🏆" and slot3 == "🏆":
                    print("Мои поздравления, Ты ВЫИГРАЛ Х2 ДЖЕКПОТ")

                elif slot1 == "💀" and slot2 == "💀" and slot3 == "💀":
                    print("Ты умрешь. Я шучу , или нет??")

                else:
                    print("Ты проиграл свой шанс")

            else:
                print("Неправильный выбор!")
            
    elif gc == "2" or gc == "К.Н.Б":
        while True:
            psr = "rock" , "paper" , "scissors"
            choicer = random.choice(psr)
            player = input("камень , ножницы или бумага?: ")
            if choicer == "rock" and player == "камень":
                print(choicer)
                print("Это ничья")
            elif choicer == "rock" and player == "ножницы":
                print(choicer)
                print("Ты проиграл :(")
            elif choicer == "rock" and player == "бумага":
                print(choicer)
                print("Ты выиграл!")
            elif choicer == "paper" and player == "бумага":
                print(choicer)
                print("Это ничья")
            elif choicer == "paper" and player == "ножницы":
                print(choicer)
                print("Ты выиграл!")
            elif choicer == "paper" and player == "камень":
                print(choicer)
                print("Ты проиграл :(")
            elif choicer == "scissors" and player == "ножницы":
                print(choicer)
                print("Это ничья")
            elif choicer == "scissors" and player == "камень":
                print(choicer)
                print("Ты проиграл :(")
            elif choicer == "scissors" and player == "камень":
                print(choicer)
                print("Ты победил!")
            else:
                print("Ошибка❌")
    elif gc == "3" or gc == "Угадай число":
        while True:
            rn = random.randint(1, 1000)
            pn = int(input("Угадай число (1 , 1000): "))
            if rn == pn:
                print(f"Моё число это {rn}")
                print("Воу, Ты победил")
            else:
                print(f"Извини но моё число было {rn}")
    else:
        print("Ошибка ❌")
        import games