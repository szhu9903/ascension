'''
121 true
-121 121- false
    # 非转字符串法 结合整数反转算法
'''

def isPalindrome(x):
    if x < 0:return False
    num = 0
    b = x
    if 10 > b:
        return True
    elif b >= 10:
        while (b > 0):
            num = num * 10 + b % 10
            b = int(b/10)
        if num == x:
            return True
        
        
        
    return False
print(isPalindrome(-5))