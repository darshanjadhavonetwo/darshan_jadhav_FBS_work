nums = [1, 2, -1, 0, -2, 1, -1, 3]
target = 2

nums.sort()
triplets = set()

for i in range(len(nums) - 2):
    a = nums[i]
    left = i + 1
    right = len(nums) - 1

    while left < right:
        b = nums[left]
        c = nums[right]
        total = a + b + c

        if total == target:
            triplets.add((a, b, c))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

if triplets:
    print("Unique triplets that sum to", target, ":")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found with the target sum.")
