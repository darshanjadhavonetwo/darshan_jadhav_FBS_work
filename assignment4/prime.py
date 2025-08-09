n=int(input("enter the number:"))
for i in range(2,(n//2)+1):
 if(n%2==0):
    print("it is not a prime number")
    break
else:
  print("it is a prime number")