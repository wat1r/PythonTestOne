from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def test_one():
    g = lambda x: x + 1

    print(g(1))
    print(g(2))

    print("*" * 40)

    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    f = filter(lambda x: x % 3 == 0, foo)
    print(list(f))

    print("*" * 40)
    m = map(lambda x: x * 2 + 10, foo)
    print(list(m))

    print(())

    return None


def test_two():
    li = [1, 2, 3, 4, 5]
    print(reduce(lambda x, y: x * y, li))
    print("*" * 40)
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print(reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9]))

    print(list(filter(lambda n: n % 2 == 1, range(1, 20))))

    print(sorted([36, 5, -12, 9, -21]))
    print(sorted([36, 5, -12, 9, -21], key=abs))

    return None


def char2num(s):
    return print(DIGITS[s])


def str2int(s):
    return print(reduce(lambda x, y: x * 10 + y, map(char2num, s)))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

@log
def now():
    print('2015-3-25')





if __name__ == '__main__':
    # test_one()
    # test_two()
    # char2num("9")
    # str2int("2")
    # f = now
    # print(f.__name__)
    now()