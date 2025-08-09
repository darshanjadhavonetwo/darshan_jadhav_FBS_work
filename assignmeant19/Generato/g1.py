def fibonacci(n):
    a,b=0,1
    while(a<=n):
        yield a
        c=a+b
        a=b
        b=c
n=int(input("enter the number:"))
print("fibonacci number up to ",n,"are:")
for i in fibonacci(n):
    print(i,end=" ")