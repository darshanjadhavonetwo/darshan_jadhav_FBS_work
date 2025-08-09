def leap():
    y=int(input("enter the year:"))
    if(y%4==0):
        print(f"{y}: it is a leap year")
    else:
        print(f"{y}: it is not leap year")

leap()