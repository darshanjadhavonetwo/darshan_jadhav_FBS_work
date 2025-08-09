n=int(input("enter the number:"))
fact=1
facts=0
for i in range(1,n+1):
    fact*=i
    facts+=fact
print("sum of factorials:",facts)