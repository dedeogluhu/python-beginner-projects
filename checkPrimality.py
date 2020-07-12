a = int(input("bir sayi giriniz"))

b = []

for i in range(1,a+1):
    if a % i == 0:
        b.append(i)
    else:
        continue

if len(b) == 2:
    print("bu asal sayidir")
else:
    print("bu asal sayi degildir veya yanlis sayi girdiniz")