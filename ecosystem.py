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

print("Ecosystem alpha starting...")

print(welcome)
print("My Github profile link : https://github.com/uzeroid666")
from datetime import datetime
time = datetime.now()
print("Current date and time:", time)

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
if choose == "1" or choose == "Calcypython":
    import Calcypython  
elif choose == "2" or choose == "Old Calculator":
    import Calcyold
elif choose == "3" or choose == "Games":
    import games
elif choose == "4" or "Calendar":
   import calendar
from datetime import datetime

print(calendar.calendar(datetime.now().year))