numbers = [5, 3, 5, 2, 3, 5, 2, 7, 3, 2, 7, 7, 5]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency dictionary:")
print(frequency)
