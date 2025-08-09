feet=int(input("enter the value of feet:"))
inches=int(input("enter the value of inches:"))
total_inches=(feet*12)+inches
centimeter=total_inches*2.54
meter=centimeter//100
centimeter=centimeter%100
print(f"centimeter is:{centimeter},meter is:{meter}")
