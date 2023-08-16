import time,functools


def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello1():
    print("Hello!")

def repeat(num):
    def my_decorator(func):
        def wrapper():
            for i in range(num):
                print("Before the function is called.")
                func()
                print("After the function is called.")
        return wrapper
    return my_decorator

@repeat(3)
def say_hello2():
    print("Hello!")

def metric(fn):
    def wrapper(*args, **kw):
        start_time = time.time()
        fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, end_time-start_time))
    return wrapper

if __name__ == '__main__':
    @metric
    def fast(x, y):
        time.sleep(0.0012)
        return x + y;


    @metric
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z;


    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')