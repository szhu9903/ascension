"""
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

"""


def removeDuplicates(nums):
    if not nums: return 0
    j = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    print(nums)
    return j + 1



if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
