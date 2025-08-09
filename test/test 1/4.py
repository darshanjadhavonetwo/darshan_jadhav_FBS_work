
interior_area = int(input("Enter interior wall area (in sq.m): "))
exterior_area = int(input("Enter exterior wall area (in sq.m): "))

interior_rate = int(input("Enter interior painting rate (per sq.m): "))
exterior_rate = int(input("Enter exterior painting rate (per sq.m): "))

interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate
total_cost = interior_cost + exterior_cost

print("Interior painting cost: ₹", round(interior_cost, 2))
print("Exterior painting cost: ₹", round(exterior_cost, 2))
print("Total painting cost: ₹", round(total_cost, 2))


 