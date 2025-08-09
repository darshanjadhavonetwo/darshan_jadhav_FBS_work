import math


radius = 20
length = 50
breadth = 40
cost_per_meter = 35
rounds = 5

half_circle_perimeter = math.pi * radius  # πr

rect_sides = length + 2 * breadth  

total_perimeter = half_circle_perimeter + rect_sides

total_wire_length = rounds * total_perimeter


if total_wire_length > 0:
    total_cost = total_wire_length * cost_per_meter
    print("Total cost of fencing the field is: ₹", round(total_cost, 2))
else:
    print("Invalid wire length. Please check input values.")
