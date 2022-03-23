# 判断是否为素数
import math
result = []
x = 1000
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

for n in range(2, x+1):
    if is_prime(n) is True:
     result.append(n)

print(result)
