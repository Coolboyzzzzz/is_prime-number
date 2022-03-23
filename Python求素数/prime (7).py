leap = 1
for i in range(2,200):
    for j in range(2,i):
        if(i%j == 0):
            leap = 0 #检测是否有因子
            break
    if leap:
        print(i)
    leap = 1
