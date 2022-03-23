def isprime(num):    #此函数用来判断一个数是否为质数
    for i in range(2,num):
        if num % 2 == 0:
            return False
    else:
        return True


for n in range(2, 200):
    if isprime(n) is True:
     print (n)
