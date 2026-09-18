games = """
                  ┌───────────────────────────┐
                  │   ┌─────────────────────┐ │
                  │   │ 1. Slot machine     │ │
                  │   │ 2. P.S.R            │ │
                  │   │ 3.Guess the number  │ │
                  │   └─────────────────────┘ │
                  └───────────────────────────┘
"""
print(games)
import random
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
    rn = random.randint(1, 1000)
    pn = int(input("Guess the number (1 , 1000): "))
    if rn == pn:
        print(f"My number is {rn}")
        print("Wow , You Win!")
        import games
    else:
        print(f"Sorry but my number is {rn}")
        import games
else:
    print("Invalid Choose ❌")
    import games