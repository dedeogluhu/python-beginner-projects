import random

x = random.randrange(0,21)

y=int(input("sayıyı tahmin ediniz(20 hakkınız var)"))

for a in range(0,21):
    if x == y:
        print("sayıyı doğru bildiniz")
        break
    elif y > x:
        print("biraz küçük salla")
    elif y < x:
        print("biraz büyük salla")
    elif y < 0 or y > 20:
        print("1 ile 20 arasında sayı gir")
    else:
        print("bir hata oluştu")
    y=int(input("yeni sayı giriniz"))
print("oyun bitti")