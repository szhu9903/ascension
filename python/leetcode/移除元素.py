"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


def removeElement(nums, val):
    num = 0
    if len(nums)==0:return 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[num] = nums[i]
            num +=1
    return num




if __name__ == '__main__':
    res = removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(res)

