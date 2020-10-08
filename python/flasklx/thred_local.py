
from threading import Thread
try:
    from greenlet import getcurrent as get_ident
except Exception:
    from threading import get_ident

class Local():

    def __init__(self):
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][key] = value
        else:
            self.storage[ident] = {key : value}

    def __getattr__(self, item):
        ident = get_ident()
        data = self.storage.get(ident, 'no ident')
        return data


loc = Local()

def task(arg):
    loc.val = arg
    print(loc.val.get('val'))

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target = task, args=(i, ))
        t.start()


