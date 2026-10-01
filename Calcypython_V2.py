from config import * 

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
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        print(error)
        return "Error: Division by zero is not allowed."
    return num1 / num2
def integer_divide(num1, num2):
    if num2 == 0:
        print(error)
        return "Error: Division by zero is not allowed."
    return num1 // num2
def exponentiate(num1, num2):
    return num1 ** num2
def modulo(num1, num2):
    if num2 == 0:
        print(error)
        return "Error: Division by zero is not allowed."
    return num1 % num2
if language == "2.en" or language == "2" or language == "en":
    print(f"Welcome to the calculator {name}")
    while True:
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
        choice = input("choose an operation (+, -, *, /, //, **, %, q to quit): ")

        if choice == "q":
            break
        if choice == "+":
            print(calculating)
            print("Result: ", add(num1, num2))
        elif choice == "-":
            print(calculating)
            print("Result: ", subtract(num1, num2))
        elif choice == "*": 
            print(calculating)
            print("Result: ", multiply(num1, num2))
        elif choice == "/":
            print(calculating)
            print("Result: ", divide(num1, num2))
        elif choice == "//":
            print(calculating)
            print("Result: ", integer_divide(num1, num2))
        elif choice == "**":
            print(calculating)
            print("Result: ", exponentiate(num1, num2))
        elif choice == "%":
            print(calculating)
            print("Result: ", modulo(num1, num2))
        else:
            print(error)
            print("Error: Invalid operation.")

elif language == "1.ru" or language == "ru" or language == "1":
    print(f"Добро пожаловать в калькулятор {name_ru}")
    while True:
        num1 = int(input("введите первое число: "))
        num2 = int(input("введите второе число: "))
        choice = input("выберите операцию (+, -, *, /, //, **, %, q чтобы выйти): ")

        if choice == "q":
            break
        if choice == "+":
            print(calculating)
            print("Результат: ", add(num1, num2))
        elif choice == "-":
            print(calculating)
            print("Результат: ", subtract(num1, num2))
        elif choice == "*":
            print(calculating)
            print("Результат: ", multiply(num1, num2))
        elif choice == "/":
            print(calculating)
            print("Результат: ", divide(num1, num2))
        elif choice == "//":
            print(calculating)
            print("Результат: ", integer_divide(num1, num2))
        elif choice == "**":
            print(calculating)
            print("Результат: ", exponentiate(num1, num2))
        elif choice == "%":
            print(calculating)
            print("Результат: ", modulo(num1, num2))
        else:
            print(error)
            print("Ошибка: Недопустимая операция.")