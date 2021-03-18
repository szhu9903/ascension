"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
"""

class Solution:
    def threeSum(self, nums):
        nums_len = len(nums)
        # 长度不符合要求 直接返回结果
        if (not nums or nums_len < 3): return []
        nums.sort()
        res = []
        for i in range(nums_len):
            if (nums[i] > 0): return res
            # 最左侧开始位置重复、右移
            if (i>0 and nums[i] == nums[i-1]): continue
            L = i + 1
            R = nums_len - 1
            while L < R:
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L<R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L<R and nums[R] == nums[R - 1]):
                        R = R-1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[R] + nums[L] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

if __name__ == '__main__':
    nums = [0, 0, 0]
    res = Solution().threeSum(nums)
    print(res)