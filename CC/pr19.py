def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

# Sample Input
nums = [1, 2, 3, 4, 5]
target = 9

# Output
print(two_sum(nums, target)) 