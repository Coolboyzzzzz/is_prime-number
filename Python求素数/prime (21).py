def primeNUM(min,max):
  if min==1:
    print('')
    min += 1
  for i in range(min, max+1):
    for j in range(2, i + 1):
      if i % j == 0:     #判断i能不能被整除
        break        #退出for循环
    if j == i:         #若j等于i，说明i是素数
      print(i,end=" ")
  print('')
primeNUM(1,200)
