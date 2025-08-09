class Book():
    def __init__(self,bid,bname,bprice,author):
        self.bid=bid
        self.bnm=bname
        self.bpri=bprice
        self.aut=author
    def showdata(self):
        print("book id:",self.bid)
        print("book name:",self.bnm)
        print("book price:",self.bpri)
        print("book author",self.aut)
        print("##############################################")
    def __del__(self):
        print("destructor is called")

b1=Book(1,"benj",120,"cnd")
del b1

        

