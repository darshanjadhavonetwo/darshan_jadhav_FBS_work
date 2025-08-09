n=int(input("enter the number:"))
n1=n
count=0
n2=n
while n2>0:
    count+=1
    n2=n2//10
    sum=0
while n>0:
    digit=n%10
    sum+=digit**count
    n=n//10
if sum== n1:
    print(n1,"is an amstrong number")
else:
    print(n1,"it is not a amstrong number")

