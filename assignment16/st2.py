class product():
    discount=10
    def __init__(self,pid,pname,price,quantity):
                product.discount+=1
                self.pid=pid
                self.pnm=pname
                self.ppri=price
                self.qua=quantity
    def showdata(self):
            print (f"product id:{self.pid}\nproduct name:{self.pnm}\nproduct price:{self.ppri}\nproduct quantity:{self.qua}")
    @staticmethod
    def totalcount():
            print("total discount",product.discount)
            #self.peri=price-=(price+product)
p1=product(1,"anu",120,3)
p1.showdata()
p2=product(2,"shbu",72,3)
p2.showdata()
p3=product(3,"sjh",1200,3)
p3.showdata()
print("########################################################")
p3.totalcount()