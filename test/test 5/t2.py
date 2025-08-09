input_data = input("Enter the total number of coins and the coin values:\n").split()
original_count = int(input_data[0])
coins = list(map(int, input_data[1:]))
frequency = {}
for coin in coins:
    if coin in frequency:
        frequency[coin] += 1
    else:
        frequency[coin] = 1
for number, count in frequency.items():
    if count % 2 != 0:
        print("The missing coin has the number:", number)
        break
