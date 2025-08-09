studen=int(input("enter the student number:"))
per=0
for i in range(1,studen+1):
    print("enter the marks for student:",i)
    total_marks=0
    for j in range(1,6):
        marks=int(input("enter the marks:"))
        total_marks+=marks
    per=(total_marks//500)*100
    print("persantage of students:",per)
    
    
    