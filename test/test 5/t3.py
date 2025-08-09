
Data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000]
]


n = len(Data)
for i in range(n):
    for j in range(0, n - i - 1):

        if Data[j][2] > Data[j + 1][2]:
           
            Data[j], Data[j + 1] = Data[j + 1], Data[j]


print("Sorted Employee List based on Salary:")
for emp in Data:
    print(emp)
