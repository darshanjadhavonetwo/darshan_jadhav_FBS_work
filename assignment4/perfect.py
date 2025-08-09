n=int(input("enter the number:"))
per=0
for i in range(1,n+1):
    if(n%i==0):
        per=per+i
    elif(per==n):
        print("it is perfect number:",n)
    else:
        print("it is not a perfect number:",n)
        
        