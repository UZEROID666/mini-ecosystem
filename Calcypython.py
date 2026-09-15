
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

lang = """
          ┌──────────────────────┐
          │   ┌────────────────┐ │
          │   │ Language       │ │ 
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
print(lang)

print("Выберите язык: Русский (ru) , english (en) , o'zbekcha (uz)")

language = input("Choose language (ru/en/uz): ")

if language == "ru":
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

elif language == "en":
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

elif language == "uz":
    while True:
   
        print("""
        + bu qo'shish
        - bu ayirish
        * bu ko'paytirish
        / bu bo'lish
        // bu butun sonli bo'lish
        ** bu darajaga ko'tarish
        % bu qoldiq
        """)

        num1 = input("Birinchi sonni kiriting: ")
        num2 = input("Ikkinchi sonni kiriting: ")
        operation = input("Amalni kiriting (+, -, *, /, //, **, %): ")
        if operation == "+":
            print(calculating)
            print('Natija: ', float(num1) + float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                print("Programma yopilishi...")
                break
        elif operation == "-":
            print(calculating)
            print('Natija: ', float(num1) - float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                            print("Programma yopilishi...")
                            break
        elif operation == "*":
            print(calculating)
            print('Natija: ', float(num1) * float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                            print("Programma yopilishi...")
                            break
        elif operation == "/":
            print(calculating)
            print('Natija: ', float(num1) / float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                print("Programma yopilishi...")
                break
        elif operation == "//":
            print(calculating)
            print('Natija: ', float(num1) // float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                print("Programma yopilishi...")
                break
        elif operation == "**":
            print(calculating)
            print('Natija: ', float(num1) ** float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                print("Programma yopilishi...")
                break
        elif operation == "%":
            print(calculating)
            print('Natija: ', float(num1) % float(num2))
            quit = input("Programmadan chiqishni istaysizmi? (yes/no): ")
            if quit == "yes":
                print("Programma yopilishi...")
                break
        else:
            print(error)