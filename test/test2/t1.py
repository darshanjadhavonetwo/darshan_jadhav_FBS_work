y=int(input("enter the year:"))
if(y%4==0):
    print("it is leap year")
elif(y%100==0):
    print("it is leap year")
elif(y%400==0):
    print('it is leap yera')
else:
    print("it is not a leap year")
    