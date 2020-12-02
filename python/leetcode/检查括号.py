
def isValid(s):
    valid_dict = {
        '(' : ')',
        '{' : '}',
        '[':']',
        '?':'?'
    }
    if len(s)%2 == 1:
        return False
    stack = ['?']
    for i in s:
        if i in valid_dict:
            stack.append(i)
        elif valid_dict[stack.pop()] != i:
            return False
    return len(stack) == 1

    # for i in range(int(len(s)/2)):
    #     if s[i] in valid_dict and len(s) % 2 == 0:
    #         if s[i + 1] == valid_dict[s[i]]:
    #             if s[i + 2:]:
    #                 return isValid(s[i + 2:])
    #             else:
    #                 return True
    #         elif s[-(i + 1)] == valid_dict[s[i]]:
    #             if s[i+1:-(i + 1)]:
    #                 return isValid(s[i + 1:-(i + 1)])
    #     break
    # return False

if __name__ == '__main__':


    print(isValid("(([]){})"))




