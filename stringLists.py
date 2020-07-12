x = input("palindrome testi yapmak istediginiz kelimeyi giriniz\n")

y = x[::-1]

if x == y:
    print("bu palindromedur")
else:
    print("palindrome degildir ya da yanlis kelime girdiniz")