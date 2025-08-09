class Book():
    def __init__(self,bid,bname,bprice,author):
        self.bid=bid
        self.bnm=bname
        self.bpri=bprice
        self.aut=author
    def display(self):
        print("book id:",self.bid)
        print("book name:",self.bnm)
        print("book price:",self.bpri)
        print("book author",self.aut)
        print("##############################################")


b1=Book(1,"benj",120,"cnd")
b1.display()
b2=Book(44,"benhbwgsj",72,"bh")
b2.display()
b3=Book(12,"benjwhu",1200,"dwnj")
b3.display()