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

    def __del__(self):
        print("it is destractor")
s1=Shirt(1,"black","formal",1200,"l")
del s1