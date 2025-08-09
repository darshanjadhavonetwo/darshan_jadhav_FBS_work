n=int(input("entere the number of passanger:"))
t_amt=int(input("enter the amt of ticket:"))
a=0
for i in range(1,n+1):
    age=int(input("enter the age of passangers:"))
    if(age<12):
        dis=t_amt*0.3
    elif(age>59):
        dis=t_amt*0.5
    else:
        dis=0
    amt=t_amt-dis
    a=a+amt
print("total amount:",a)
   
       


        
        
        

   