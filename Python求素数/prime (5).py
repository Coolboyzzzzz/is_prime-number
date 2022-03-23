import math
import time
ss = []  #  放可能是素数的列表
fss = []  # 放可能是非素数的列表
result = []  # 最终结果
x = 300
# 遍历所有小于X，大于2的数
for xx in range(2, x+1):
    # 只要xx的数，不能被2至xx的平方根的所有数整除，就是素数
    for i in range(2, int(math.sqrt(xx)+1)):
        if (xx % i) != 0:
            i = i + 1
            # print("素数: ",xx)
            ss.append(xx)
        else:
            # print("非素数", xx)
            fss.append(xx)

# 只要x中的数没有出现在非素数列表中，则它就是素数
for j in range(2, x+1):
    if j not in fss:
        result.append(j)

print("result: ", result)
