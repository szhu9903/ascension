class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:return 0
        return haystack.index(needle) if needle in haystack else -1
    def strStr1(self, haystack: str, needle: str):
        hays_len = len(haystack)
        needle_len = len(needle)
        if needle_len == 0:return 0
        if needle_len <= hays_len:
            for i in range(hays_len - needle_len + 1):
                if needle == haystack[i:i + needle_len]:
                    return i
        return -1
if __name__ == '__main__':
    index_num = Solution().strStr1('hello', '')
    print(index_num)
