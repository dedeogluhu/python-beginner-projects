x = input("Adınızı giriniz")
y = int(input("Yaşınızı Giriniz"))

if type(x) == str:
    if type(y) == int:
        print( x, " Bey/Hanım şuan ", y, "yaşındasınız ve ", 100 - y, "yıl sonra 100 yaşında olacaksınız.")
    else:
        print("lütfen bir sayı giriniz")
else:
    print("lütfen isminizi giriniz")
