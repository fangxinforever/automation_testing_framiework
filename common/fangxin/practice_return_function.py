def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count_new():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

if __name__ == '__main__':
    f = lazy_sum(1, 3, 5, 7, 9)
    f1, f2, f3 = count_new()
    f = inc()
    print(f())  # 1
    print(f())  # 2
