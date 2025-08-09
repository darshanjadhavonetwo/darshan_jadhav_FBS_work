a=int(input("enter the  side 1:"))
b=int(input("enter the  side 2:"))
c=int(input("enter the  side 3:"))
if(a+b>c):
    if(a+c>b):
        if(b+c>a):
            print("triangle is valide")
else:
    print("trangle is invalide")            