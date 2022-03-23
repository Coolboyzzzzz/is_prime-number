import math
def countPrimes2(self, n):
  if n<=2:
   return 0
  else:
   res=[]
  for i in range(2, n):
   flag=0
   for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
     flag = 1
   if flag == 0:
    res.append(i)
  return res

print(countPrimes2(2,1000))
