#fibonacci --> i = (i-1) + (i-2)

a = int(input("kac sayilik bir seri oluşturalım"))

b = [1,1]

for i in range(1,a-1):
    b.append(b[i]+b[i-1])

print(b)