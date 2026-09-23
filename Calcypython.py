
calculating = """
          ┌──────────────────────┐
          │   ┌────────────────┐ │
          │   │ Calculating... │ │
          │   └────────────────┘ │
          │                      │
          │   ─── ─── ───   ───  │
          │  │ 7 │ 8 │ 9 │ │ + │ │
          │  ├───┼───┼───┤ ├───┤ │
          │  │ 4 │ 5 │ 6 │ │ − │ │
          │  ├───┼───┼───┤ ├───┤ │
          │  │ 1 │ 2 │ 3 │ │ x │ │
          │  ├───┼───┼───┤ ├───┤ │
          │  │ · │ 0 │ = │ │ / │ │
          │  └───┴───┴───┘ └───┘ │
          └──────────────────────┘
"""

error = """
          ┌──────────────────────┐
          │   ┌────────────────┐ │
          │   │ Error!         │ │ 
          │   └────────────────┘ │
          │                      │
          │   ─── ─── ───   ───  │
          │  │ 7 │ 8 │ 9 │ │ + │ │
          │  ├───┼───┼───┤ ├───┤ │
          │  │ 4 │ 5 │ 6 │ │ − │ │
          │  ├───┼───┼───┤ ├───┤ │
          │  │ 1 │ 2 │ 3 │ │ x │ │
          │  ├───┼───┼───┤ ├───┤ │
          │  │ · │ 0 │ = │ │ / │ │
          │  └───┴───┴───┘ └───┘ │
          └──────────────────────┘
"""

from config import language

if language == "1.ru" or language == "ru" or language == "1":
    from config import name_ru
    print(f"{name_ru} Добро пожаловать")
    while True:
   
        print("""
        + это плюс
        - это минус
        * это умножение
        / это деление
        // это целочисленное деление
        ** это возведение в степень
        % это остаток от деления
        """)

        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        operation = input("Введите действие (+, -, *, /, //, **, %): ")
        if operation == "+":
            print(calculating)
            print('Результат: ', float(num1) + float(num2))
            quit = input("Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        elif operation == "-":
            print(calculating)
            print('Результат: ', float(num1) - float(num2))
            quit = input("Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        elif operation == "*":
            print(calculating)
            print('Результат: ', float(num1) * float(num2))
            quit = input("Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        elif operation == "/":
            print(calculating)
            print('Результат: ', float(num1) / float(num2))
            quit = input("Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        elif operation == "//":
            print(calculating)
            print('Результат: ', float(num1) // float(num2))
            quit = input("Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        elif operation == "**":
            print(calculating)
            print('Результат: ', float(num1) ** float(num2))
            quit = input(" Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        elif operation == "%":
            print(calculating)
            print('Результат: ', float(num1) % float(num2))
            quit = input("Вы хотите выйти из программы? (yes/no): ")
            if quit == "yes":
                        print("Выход из программы...")
                        break
        else:
            print(error)


elif language == "2.en" or language == "2" or language == "en":
    from config import name
    print(f"{name} Welcome")
    while True:
   
        print("""
        + is plus
        - is minus
        * is multiplication
        / is division
        // is integer division
        ** is exponentiation
        % is modulus
        """)

        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        operation = input("Enter the operation (+, -, *, /, //, **, %): ")
        if operation == "+":
            print(calculating)
            print('Result: ', float(num1) + float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        elif operation == "-":
            print(calculating)
            print('Result: ', float(num1) - float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        elif operation == "*":
            print(calculating)
            print('Result: ', float(num1) * float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        elif operation == "/":
            print(calculating)
            print('Result: ', float(num1) / float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        elif operation == "//":
            print(calculating)
            print('Result: ', float(num1) // float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        elif operation == "**":
            print(calculating)
            print('Result: ', float(num1) ** float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        elif operation == "%":
            print(calculating)
            print('Result: ', float(num1) % float(num2))
            quit = input("Do you want to quit? (yes/no): ")
            if quit == "yes":
                print("Exiting the program...")
                break
        else:
            print(error)