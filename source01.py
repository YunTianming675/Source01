import time

def timeit(iteraction):
    def inner(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iteraction):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret
        return wrapper
    return inner


@timeit(1000)
def double(x):
    return x * 2


# double(2)等价于
inner = timeit(1000)
double = inner(double)

print(double(2))
