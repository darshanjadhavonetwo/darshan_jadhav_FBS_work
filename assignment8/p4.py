def odd():
    n=int(input("enter the number:"))
    for i in range(1,n):
        if(i%2==1):
            print(i,end=" ")
odd()