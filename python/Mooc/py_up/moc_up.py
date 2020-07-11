
def format_name(name):
    return name[0].upper() + name[1:].lower()

if __name__ == '__main__':
    new_name = map(format_name,['admin','LISA','brRt'])
    print(list(new_name))






