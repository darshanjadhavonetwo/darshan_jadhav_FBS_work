for i in range(10):  # 10 rows (0 to 9)
    for j in range(21):  # 10 columns (0 to 9)
        if i == 0 or i == 9:
            print("*", end="")  # Top and bottom rows
        elif j == 20 - i :
            print("*", end="")  # Diagonal from top-right to bottom-left
        else:
            print(" ", end="")  # Space elsewhere
    print()






