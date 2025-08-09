ticket_price = float(input("Enter ticket price per person: "))

total_amount = 0

# Loop to accept age of 5 people
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    
    if age < 12:
        # 30% discount
        discounted_price = ticket_price * 0.70
    elif age > 59:
        # 50% discount
        discounted_price = ticket_price * 0.50
    else:
        # Full price
        discounted_price = ticket_price
    
    total_amount += discounted_price

# Display the total amount
print(f"\nTotal ticket amount for 5 people: ₹{total_amount:.2f}")