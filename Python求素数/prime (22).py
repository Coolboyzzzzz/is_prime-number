def test(num):
  list = []       #定义一个列表 用于存储计算的数
  i = num -1       # 去除本身
  while i > 1:      # 去除1 https://blog.zeruns.tech
    if num %i == 0 :  #判断是否有余数
      list.append(i) # 将所有的能整除i的数加入列表
    i -= 1
  if len(list) == 0 and num != 1:   # 如果列表为空 就是表示除了1和它本身能整除
    print(num,end=' ')

def primeNUM2(min,max):
  j = min
  while j < max:
    test(j)
    j += 1
  print('')
primeNUM2(1,100)
