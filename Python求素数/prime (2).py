# 构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
def _not_visible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_visible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
