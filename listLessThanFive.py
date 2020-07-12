x = [2,6,3,23,4,1]

while True:
    y = input("listeye istediğiniz kadar sayı ekleyiniz \nbitince bitti yazınız\n")
    if str(y) == "bitti" or str(y) == "Bitti":
        break
        print(x)
    x.append(int(y))

x.sort()

for i in range(0,len(x)):
    if x[i] <= 5:    
        print(x[i])

print(x)