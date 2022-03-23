def countPrimes3(self, n):
  if n <= 2:
   return 0
  else:
   res = []
  for i in range(2, n):
   flag = 0
   for j in res:
    if i % j == 0:
     flag = 1
   if flag == 0:
    res.append(i)
  return res

print(countPrimes3(2,1000))
