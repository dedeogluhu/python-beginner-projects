import random

while True:
    x = random.randrange(1,7)
    print(str(x))
    y = int(input("\n0. zar atma \n1. tekrar zar at"))
    if y == 0:
        break
    elif y == 1:
        continue
    else:
        print("1 veya 0 giriniz")
    
