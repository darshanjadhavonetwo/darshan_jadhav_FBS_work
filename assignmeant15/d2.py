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
    def __del__(self):
        print("it is destructor")

p1=product(1,"anu",120,3)
del p1
