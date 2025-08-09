a1=int(input("enter the value of a1:"))
a2=int(input("enter the value of a2:"))
a3=int(input("enter the value of a3:"))
a4=int(input("enter the value of a4:"))
a5=int(input("enter the value of a5:"))
amt=int(input("enter the amt :"))
if(a1<12):
    dis=amt*30/100   
    total_amt=amt-dis
    print("pay payment 30%:",total_amt)  
elif(a3>59):
    dis=amt*50/100   
    total_amt=amt-dis
    print("pay payment 50%:",total_amt) 
    
else:
    print("other need to pay full payment")



