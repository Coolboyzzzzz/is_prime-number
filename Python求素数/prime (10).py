# 求 a~b之间的素数
def su(a,b):
    for i in range(a,b):
        n = False #默认不是素数，如果是素数，跳出循环
        for j in range(2,i):
            if i%j == 0:
                n = True
                break
                
        if n == False:
            print(i,end=" ")

su(100,200)
