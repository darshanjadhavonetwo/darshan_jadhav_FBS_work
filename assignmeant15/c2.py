class product():
    def __init__(self,pid,pname,pprice,quantity):
        self.pid=pid
        self.pnm=pname
        self.ppri=pprice
        self.qua=quantity
    def display(self):
        print("product id:",self.pid)
        print("product name:",self.pnm)
        print("product price:",self.ppri)
        print("product quantity",self.qua)
        print("##############################################")


p1=product(1,"anu",120,3)
p1.display()
p2=product(2,"shbu",72,3)
p2.display()
p3=product(3,"sjh",1200,3)
p3.display()