x = int(input("bir sayı giriniz"))

while True:
    if x % 2 == 0:
        print("bu sayı bir çift sayıdır")
    elif x % 2 == 1:
        print("bu sayı bir tek sayıdır")
    else:
        print("lütfen bir sayı giriniz")
    x = int(input("yeni bir sayı girebilirsiniz"))