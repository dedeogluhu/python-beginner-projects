
# %% Character input


x = input("Enter your name")
y = int(input("Enter your age"))
z = int(input("How many times do you want me to print "))

for i in range(0, z):
    print("You will turn 100 at {}".format((2020 + (100-y))))

# %% Odd or Even

number = int(input("Give me the number you want to know if odd or even"))

if number % 2 == 0:
    print("Even")
    if number % 4 == 0:
        print("This is a multiple of 4")
elif number % 2 == 1:
    print("Odd")

# %% Less Then 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = list()
c = int(input("Kaçtan küçük sayıları yazdırayım?"))

for i in a:
    if i < c:
        b.append(i)

print(b)

# %% Divisors

x_four = int(input("whiich number you want me to print divisors of ?"))

for i in range(1, x_four):
    if x_four % i == 0:
        print(i)

# %% List Overlap
import random

def randomList(a):
    for i in range(0, 10):
        a.append(random.randint(1, 100))


q = list()
w = list()

randomList(q)
randomList(w)

q_s = set(q)
w_s = set(w)

c = list(q_s.intersection(w_s))

print(c)

# %% String Lists

x = input("Pls enter a string")

y = x[::-1]

if y == x:
    print("this is a palindrome")
else:
    print("this is not a palindrome")

# %% List Comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = list()

for i in a:
    if i % 2 == 0:
        b.append(i)

print(b)

# %% Rock Paper Scissors

# 0 -> rock   ,   1 -> paper     ,    2 -> scissors
import random

def game():
    while True:
        a = int(input("Taş Kağıt Makas ?\n0.rock\n1.paper\n2.scissors\n3.exit"))
        b = random.randrange(0, 3)
        
        if a == 0:
            if b == 0:
                print("u r even, again")
            elif b == 1:
                print("u lose")
            elif b == 2:
                print("u win congratz big boy")

        elif a == 1:
            if b == 0:
                print("u win congratz")
            elif b == 1:
                print("u r even, again")
            elif b == 2:
                print("u lose")

        elif a == 2:
            if b == 0:
                print("u lost haha")
            elif b == 1:
                print("u win wow")
            elif b == 2:
                print("again")

        elif a == 3:
            break

        else:
            print("wrong choice boy")


game()

#%% Guessing Game One

import random


def guess():
    
    x = random.randrange(1,10)

    for i in range(0,20):
    
        y = int(input("guess my number"))
        
        if y > x:
            print("too high")
        elif y < x:
            print("too low")
        elif y == x:
            print("you found it")
            print("it took {} guesses to find".format(i))
            break
            
        else:
            print("wrong")
    else:
        print("u couldn't")

guess()

#%% List Overlap Comprehensions