import math


def get_prime():
    num = 2

    while True:
        if is_prime(num):
            yield num
        num += 1



def is_prime(value):
    result = True
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result
for prime in get_prime():
    print(prime)
#这里就算出100以内的，超过100就跳出
    if prime > 100:
        break
