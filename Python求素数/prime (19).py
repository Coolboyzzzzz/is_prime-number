def handlerNum(num):
 # 质数大于 1
 if num > 1:
  # 查看是否有其他因子
  for i in range(2, num//2+1):
   if (num % i) == 0:
    print(num,"不是质数")
    break
  else:
   print(num, "是质数")

 # 如果输入的数字小于或等于 1，不是质数
 else:
  print(num, "不是质数")

  # 调用函数处理方法
for i in range(2,200): 
  handlerNum(i)
