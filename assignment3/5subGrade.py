sub1=int(input("enter the marks of sub1:"))
sub2=int(input("enter the marks of sub2:"))
sub3=int(input("enter the marks of sub3:"))
sub4=int(input("enter the marks of sub4:"))
sub5=int(input("enter the marks of sub5:"))
sum=sub1+sub2+sub3+sub4+sub5
if(sum>=400):
    print("it is grade is first class")
elif(sum>=300):
    print("it  is grade is second class")
elif(sum>=200):
    print("it is grade is third class")
else:
    print("it is fail")