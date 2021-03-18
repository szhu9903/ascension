"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9
"""


def twoSum(nums, target):
    nums_len = len(nums)
    for i in range(nums_len):
        num = target - nums[i]
        if num in nums and i != nums.index(num):
            return [i, nums.index(num)]
        else:
            continue
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 6, 6, 1]

    target = 12
    d = twoSum(nums, target)
    print(d)

