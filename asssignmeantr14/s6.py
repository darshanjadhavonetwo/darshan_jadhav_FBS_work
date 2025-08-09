def max_product_pair(numbers):
    num_set = set(numbers)
    num_list = list(num_set) 
    max_product = float('-inf')
    pair = (None, None)

    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            product = num_list[i] * num_list[j]
            if product > max_product:
                max_product = product
                pair = (num_list[i], num_list[j])

    print("Two numbers with maximum product:", pair)
    print("Maximum product:", max_product)

numbers = [3, 5, -10, 4, -20, 5, 3]
max_product_pair(numbers)
