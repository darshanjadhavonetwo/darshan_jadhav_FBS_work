n=int(input("enter the number:"))
temp=n
str=0
for i in range(1,n+1):
    a=1
    a*=i
    str+=a
    if(str==temp):
        print("it is strong number:",n)
    else:
        print("it is not a strong number:",n)

