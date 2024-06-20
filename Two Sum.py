#Given an array of integers, return whether the array has two numbers that can sum to a target

nums = [1, 3, 8, 5]
target = 10

def two_sum(nums, target):
    numslen = len(nums)
    for i in range(numslen):
        for j in range(i+1, numslen):
            if nums[i] + nums[j] == target:
                return (True)

    return (False)

# two_sum(nums, target)
