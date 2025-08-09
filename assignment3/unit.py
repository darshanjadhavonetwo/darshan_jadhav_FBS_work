unite=int(input("enter the charge:"))
bill=0
if(unite<=50):
    bill=50*0.50
elif(unite<=150):
   bill=(50*0.5)+((unite-50)*0.75)
elif(unite<=250):
    bill=(50*0.5)+(100*0.75)+((unite-150)*1.20)
elif(unite>250):
    bill=(50*0.5)+(100*0.75)+(100*1.20)+((unite-250)*1.50)
    surcharge=bill*20/100
    t_bill=surcharge+bill
    print("total electric city bill= rs:",t_bill)

    
   
    