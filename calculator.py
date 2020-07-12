while True:
    t = int(input("\nEnter 0.Exit\n1.Add\n2.Minus\n3.Multiply\n4.Divide\n"))
    x,y = map(int,input("Enter two numbers    \n").split())
    if t==1:
        print("sum is\n")
        print(x+y)
    elif t==2:
        print("first number - second number is\n")
        print(x-y)
    elif t==3:
        print("Multiplication is\n")
        print(x*y)
    elif t==4:
        print("division is\n")
        print(x/y)
    elif t==0:
        break
    else:
        print("Invalid input!\n")