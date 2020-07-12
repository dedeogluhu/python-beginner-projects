import math

size = int(input("kaç karelik görünüm istiyorsunuz???"))
x = int(math.sqrt(size))

#print(" ---\n|   |\n --- ")

def cizgi():
    print("-" * 3,end = "")
    
def bosluk(a):
    print(" " * a,end = "")
    
def dik():
    print("|",end = "")

def altagec():
    print("")
    
#bosluk(1)
#cizgi()
#altagec()
#dik()
#bosluk(3)
#dik()
#altagec()
#bosluk(1)
#cizgi()
    
def cizgiler():
    for i in range(0, x):
        bosluk(1)
        cizgi()
        
    altagec()
    
def dikler():
    for i in range(0, x + 1):
        dik()
        bosluk(3)
    altagec()
    
def satir(a):
    for i in range(a):
        cizgiler()
        dikler()
    cizgiler()
       
satir(x)


