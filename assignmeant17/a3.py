class student:
    def __init__(self,id,name,age,per):
        self.id=id
        self.nm=name
        self.age=age
        self.per=per
    def calculate_m(self):
        if self.per>=90:
            return"a"
        elif self.per>=70:
            return"b"
        elif self.per>=50:
            return"c"
    def __str__(self):
        return f"id:{self.id}\nname:{self.nm}\nage:{self.age}\npersantage{self.per}"
class medicalstudent(student):
    def __init__(self, id, name,age, per,specilization,intership_marks):
        super().__init__(id,name, age, per)
        self.spe=specilization
        self.im=intership_marks
    def accept(self):
        self.id=int(input("enter the studenid:"))
        self.nm=int(input("enter the name of student:"))
        self.age=int(input("enter the age of student:"))
        self.per=int(input("enter the per:"))
        self.spe=int(input("eneter the specialization:"))
        self.im=int(input("enter the intership marks:"))
    def display(self):
        print(f"id:{self.id}\nname:{self.nm}\nage{self.age}\nper:{self.per}\nspecilization:{self.spe}\nintership marks:{self.im}")
    def calculate_m(self):
        t=self.per+(self.im*0.3)
        if self.per>=90:
            return"a"
        elif self.per>=70:
            return"b"
        elif self.per>=50:
            return"c"
    def __str__(self):
                return (f"MedicalStudent[ID: {self.id}, Name: {self.nm}, Age: {self.age}, "
                f"Percentage: {self.per}, Specialization: {self.spe}, "
                f"Internship Marks: {self.im}]")
    
m1=medicalstudent(1,"darshan",21,80.0,"eyes",12)
m1.display()
print(m1)
        

    