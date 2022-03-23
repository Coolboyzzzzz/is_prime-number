#处理函数
def IsPrime(num): #根据质数的定义，其必须大于0
 if num == 1:
  return False #循环需要判断的次数
 for i in range(2, num // 2 + 1):#如果该数有其他的因子返回False，即不是质数
  if num % i == 0:
   return False
 return True

  # 调用函数处理方法
for i in range(2,200): 
  if IsPrime(i) is True:
      print(i)
