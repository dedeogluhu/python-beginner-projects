a = int(input("Enter a number"))

b = []

for i in range(1,a+1):
    if a % i == 0:
        b.append(i)
    else:
        continue

if len(b) == 2:
    print("This is a prime number")
else:
    print("This is not a prime number")
