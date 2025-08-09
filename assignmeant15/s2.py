class product():
    def __init__(self,pid,pname,pprice,quantity):
        self.pid=pid
        self.pnm=pname
        self.ppri=pprice
        self.qua=quantity
    def showdata(self):
        print("product id:",self.pid)
        print("product name:",self.pnm)
        print("product price:",self.ppri)
        print("product quantity",self.qua)
        print("##############################################")


p1=product(1,"anu",120,3)
p1.showdata()
p2=product(2,"shbu",72,3)
p2.showdata()
p3=product(3,"sjh",1200,3)
p3.showdata()