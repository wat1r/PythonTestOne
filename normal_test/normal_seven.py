from collections import Iterable

def test_one():
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, ":", value)

    res = [m + n for m in 'ABC' for n in 'XYZ']
    print(res)
    L = ['Hello', 'World', 'IBM', 'Apple']
    res_1 = [s.lower() for s in L]
    print(res_1)

    g = (x * x for x in range(10))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

def test_two():
    # print(isinstance([],Iterable))
    # assert isinstance([],Iterable)
    # assert isinstance(100,Iterable)
    # 首先获得Iterator对象:
    it = iter([1, 2, 3, 4, 5])
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break


if __name__ == '__main__':
    # test_one()
    test_two()
