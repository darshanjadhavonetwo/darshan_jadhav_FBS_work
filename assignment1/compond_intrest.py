P=int(input("enter the value of P:"))
R=int(input("enter the value of R:"))
T=int(input("enter the value of T:"))
A=P*(1+R/100)**T
CI=A-P
print("total amount of after:",A)
print("value of compound interest:",CI)