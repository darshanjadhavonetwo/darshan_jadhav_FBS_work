class Shirt():
    def __init__(self,sid,sname,type,sprice,size):
        self.sid=sid
        self.snm=sname
        self.ty=type
        self.pri=sprice
        self.s=size
    def display(self):
        print("shirt id:",self.sid)
        print("shirt name:",self.snm)
        print("shirt type:",self.ty)
        print("shirt price",self.pri)
        print("shirt size:",self.s)
        print("##############################################")


s1=Shirt(1,"black","formal",1200,"l")
s1.display()
s2=Shirt(2,"black","informal",1200,"xl")
s2.display()
s3=Shirt(3,"white","formal",1200,"m")
s3.display()