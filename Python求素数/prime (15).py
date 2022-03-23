def countPrimes1(self, n):
  """
  :type n: int
  :rtype: int
  """
  if n<=2:
   return 0
  else:
   res=[]
  for i in range(2,n):
   flag=0 # 质数标志，=0表示质数
   for j in range(2,i):
    if i%j ==0:
     flag=1
   if flag==0:
    res.append(i)
  return res

print(countPrimes1(2,1000))
