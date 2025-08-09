sec=int(input("enter the value of sec:"))
hr=sec//3600
sec1=sec%3600
min=sec1//60
sec2=sec1%60
second=sec2//60
print(f"TIME: hr {hr},min {min},second {second}")