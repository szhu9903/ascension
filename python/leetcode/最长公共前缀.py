"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""

def longestCommonPrefix(strs):
    if strs:
        # 找出差异最大的另个字符串
        str_max = max(strs)
        str_min = min(strs)
        # 找出差异
        for i in range(len(str_min)):
            if str_max[i] != str_min[i]:
                return str_min[:i]
        return str_min
    else:
        return ""




if __name__ == '__main__':
    num = longestCommonPrefix(["flower","flow","flight"])
    print(num)
