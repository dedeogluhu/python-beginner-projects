def cizgicek(adet):
    for i in range(int(adet)):
        print("/",end="")

def terscizgi(adet):
    for i in range(int(adet)):
        print("\\",end="")
        
def bosluk(adet):
    for i in range(int(adet)):
        print("*",end="")
        
def altain():
    print()
    
def ust(cap):
    baslangic = cap/2-1
    for i in range(int(cap/2)):
        bosluk(baslangic-i)
        cizgicek(1)
        bosluk(i*2)
        terscizgi(1)
        altain()
        
    
def alt(cap):
    baslangic = cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        terscizgi(1)
        bosluk(baslangic - i * 2)
        cizgicek(1)
        altain()

def paralelkenar(cap):
    ust(cap)
    alt(cap)
        
paralelkenar(10)
paralelkenar(8)
paralelkenar(6)
paralelkenar(4)
paralelkenar(2)
        
        
