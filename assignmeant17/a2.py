class students():
    def __init__(self,id,nm,age,per):
        self.id=id
        self.nm=nm
        self.age=age
        self.per=per
    def calculate_rank(self):
        if self.per>=90:
            return"a"
        elif self.per>=75:
            return"b"
        elif self.per>=60:
            return"c"
        else:
            return"d"
    
    def __str__(self):
        return f'id:{self.id}\nname:{self.nm}\nage:{self.age}\npersantage:{self.per}'
class enggstudent(students):
    def __init__(self, id, nm, age, per,branch,internal_marks):
        super().__init__(id, nm, age, per)
        self.branch=branch
        self.im= internal_marks
    def accept(self):
        self.id=int(input("enter the student id:"))
        self.nm=int(input("enter the student name:"))
        self.age=int(input("enter the age of student:"))
        self.per=int(input("enter the persantage:"))
        self.branch=int(input("enter the branch:"))
        self.im=int(input("enter the internal marks:"))
    def display(self):
        return f'student id:"{self.id},name:{self.nm},age:{self.age},persantage:{self.per},branch:{self.branch},internal marks:{self.im}'
    def calculate_rank(self):
        t_s=self.per+(self.im*0.2)
        if self.per>=90:
            return"a"
        elif self.per>=75:
            return"b"
        elif self.per>=60:
            return"c"
        else:
            return"d"
    def ___str__(self):
        return f"enggstuden[id:{self.id}\nname:{self.nm}\nage:{self.age}\npersantage:{self.per}\nbranch:{self.branch}\ninternalmarks{self.im}]"
     
s1=enggstudent(1,"darshan",21,70.5,"python",11)
s1.display()
print(s1)