
def test(x):
    try:
        if x in [1,2]:
            return 1
        else:
            return test(x - 1) + test(x - 2)
    except Exception as er:
        print(er)



if __name__ == '__main__':
    print(test(5))