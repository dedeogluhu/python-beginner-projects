x = input("uzun bir cumle giriniz")

def ayir(a):
    return a.split()

y = ayir(x)

y.reverse()

z = ' '.join(y)

print(z)

#def reverseWord(w):
#  return ' '.join(w.split()[::-1])