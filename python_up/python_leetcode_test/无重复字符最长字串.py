

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

"""
# 滑动窗口算法szhu
def lengthOfLongestSubstring(s):
    if len(s) <= 0:return 0
    max_str = ''
    max_len = 0
    for i in s:
        if i in max_str:
            max_str = max_str[max_str.index(i)+1:]
        max_str += i
        if max_len < len(max_str):max_len=len(max_str)
    return max_len

# 滑动窗口算法 标准版
def lengthOfLongestSubstring1(s):
    """
    双指针组成滑动窗口
    """
    if len(s) <= 0:return 0
    left = 0 # 左指针位置,右指针利用循环指针
    num_data = set()
    max_len = 0
    cur_len = 0
    for i in range(len(s)):
        cur_len += 1
        # 当前元素存在窗口中，左指针移动到重复位置
        while s[i] in num_data:
            num_data.remove(s[left])
            # 做指针右滑动
            left += 1
            # 记录数量递减
            cur_len -= 1
        if cur_len > max_len:max_len = cur_len
        num_data.add(s[i])
    return max_len

if __name__ == '__main__':
    res = lengthOfLongestSubstring1(' nnnko')
    print(res)



