import random

x = random.randrange(0,21)

y=int(input("You have 20 turns to guess the number"))

for a in range(0,21):
    if x == y:
        print("You guessed right")
        break
    elif y > x:
        print("A bit smaller")
    elif y < x:
        print("A bit bigger")
    elif y < 0 or y > 20:
        print("Enter a number between 20")
    else:
        print("Enter a valid number")
    y=int(input("Guess again"))
print("Game Over")
