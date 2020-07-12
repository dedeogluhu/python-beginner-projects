import random

#0 = rock 1 = paper 2 = scissors

x = random.randrange(0,3)
y = "oyunbaşı"
z = int(input("\n 0 = rock \n 1 = paper \n 2 = scissors"))

while True:
    if z == 0:
        if x == 0:
            print("berabere")
        elif x == 1:
            print("kağıt taşı sarar, you lose")
        elif x == 2:
            print("taş makası kırar, you win")
    elif z == 1:
        if x == 0:
            print("kağıt taşı sarar, you win")
        elif x == 1:
            print("berabere")
        elif x == 2:
            print("makas kağıdı keser, you lose")
    elif z == 2:
        if x == 0:
            print("taş makası kırar, you lose")
        elif x == 1:
            print("makas kağıdı keser, you win")
        elif x == 2:
            print("berabere") 
    else:
        print("yanlış numara girdiniz")
    z = int(input("yeni bir satı giriniz"))
    x = random.randrange(0,3)