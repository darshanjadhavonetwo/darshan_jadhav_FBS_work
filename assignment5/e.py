x=int(input("enter the value of x:"))
n=int(input("enter the number of term:"))
s=0
si=1
den=1
for i in range(1,n+1):
    si*=-1
    den+=2
    s+=si*(x**i)/den
    print(s)
