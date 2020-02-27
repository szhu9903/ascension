
def test(x):
    try:
        if x in [1,2]:
            return 1
        else:
            return test(x - 1) + test(x - 2)
    except Exception as er:
        print(er)


def test1(a,n):
    try:
        num = a
        for i in range(n - 1):
            num = num * a
        return num
    except Exception as er:
        print(er)

if __name__ == '__main__':
    # print(test(5))
    print(test1(1,0))