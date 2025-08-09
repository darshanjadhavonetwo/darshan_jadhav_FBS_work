p1=int(input("enter the product1 price:"))
p2=int(input("enter the product2 price:"))
p3=int(input("enter the product3 price:"))
p4=int(input("enter the product4 price:"))
p5=int(input("enter the product5 price:"))
t_p=p1+p2+p3+p4+p5
gst=t_p//18*100
t_a=t_p+gst
if(t_a==0):
    print(f"{t_a} it is total bill of shoping")
else:
    print(f"{t_a} it is not sorted")
