class students():
    def __init__(self,id,nm,age,per):
        self.id=id
        self.nm=nm
        self.age=age
        self.per=per
    def calculate(self):
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
s1=students(1,"darshan",21,10)
s1.calculate()
print('#####################################################')
s2=students(2,"dqrshhh",22,10)
s2.calculate()
s2(s2.__dict__)