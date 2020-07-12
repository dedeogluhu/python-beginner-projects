x = [1,1,3,5,6,6,7,8,5,5,9]

def removeDupli(a):
    return list(dict.fromkeys(a))

y = removeDupli(x)

print (y)