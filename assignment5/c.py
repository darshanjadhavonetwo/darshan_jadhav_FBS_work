n=int(input("enter te number:"))
s=0
t=1
for i in range(1,n+1):
    t*=2
    s+=t
    print(s)
