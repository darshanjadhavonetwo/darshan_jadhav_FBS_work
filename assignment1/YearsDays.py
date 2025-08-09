total_d=int(input("enter the value of days:"))
year=total_d//365
remaing=total_d%365
week=remaing//7
days=remaing%7
print(f"days:{total_d}=year:{year},week:{week},days:{days}")
