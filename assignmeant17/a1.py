class student ():
    add=0
    def __init__(self,id,nm,age,per):
        student.add+=1
        self.id=id
        self.nm=nm
        self.age=age
        self.per=per
    def showdata(self):
        print("student id:",self.id)
        print("student name:",self.nm)
        print("student age:",self.age)
        print("per:",self.per)
    @staticmethod
    def totalcount():
        print("total count",student.add)
s1=student(1,"darshan",21,10)
s1.showdata()
print('#####################################################')
s2=student(2,"dqrshhh",22,10)
s2.showdata()
s2.totalcount()

