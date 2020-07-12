import string
import random

plength = int(input("sifre kac haneli olsun?"))

x = string.ascii_letters + string.digits * 3 

password = []

for i in range (1,plength + 1):
    password.append(random.choice(x))
    
print("".join(password))