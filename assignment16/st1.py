class Book():
    add=0
    def __init__(self,bid,bname,price,author):
        Book.add+=1
        self.id=bid
        self.bnm=bname
        self.price=price
        self.author=author
    def showdata(self):
        print(f"id:{self.id}\nbook name:{self.bnm}\nprice:{self.price}\nauthor:{self.author}")
    def totalcount():
        print("total count",Book.add)

b1=Book(1,"benj",120,"cnd")
b1.showdata()
b2=Book(44,"benhbwgsj",72,"bh")
b2.showdata()
b3=Book(12,"benjwhu",1200,"dwnj")
b3.showdata()
Book.totalcount()