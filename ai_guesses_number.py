import random

x = 0
y = 100
counter = 0 

print("choose a number between 0-100 and let me guess your number")

while True:
    a = random.randint(int(x),int(y))

    print("your number is", a, end = "  ")

    guess = int(input("1.too low\n2.too high\n3.congratulations"))
        
    if guess == 3:
        print("thank you for playing the game\nit took ", counter, " guesses to find your number")
        break
    
    elif guess == 2:
        y = a
    
    elif guess == 1:
        x = a
    
    counter += 1

print("Game's Over")
    
    
    
    