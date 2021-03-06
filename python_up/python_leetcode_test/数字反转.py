"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""
def reverse(self, x: int) -> int:
    if -10 < x < 10:
        return x
    if x >= 0:
        num_list = list(str(x))
        num = ''.join(num_list[::-1])
    else:
        num_list = list(str(abs(x)))
        num = '-' + ''.join(num_list[::-1])
    n = int(num)
    if -2147483648 < n < 2147483647:
        return n
    return 0

# TODO 待处理
# if __name__ == '__main__':
#     a = 'aabbccddeeffabcddbca'   #abcd
#     a_bytes = bytes.fromhex(a)
#     print(a)





