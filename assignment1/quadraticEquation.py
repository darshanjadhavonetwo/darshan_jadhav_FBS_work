#Program to Find the Roots of a Quadratic Equation
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
D=(b**2)-(4*a*c)
Q1=(-b+D**0.5)/(2*a)
Q2=(-b-D**0.5)/(2*a)
print(F"root of equation are: q1:{Q1},q2:{Q2}")