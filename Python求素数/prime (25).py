def isPrime(n): 
  if n <= 1: 
    return False
  if n == 2: 
    return True
  if n % 2 == 0: 
    return False
  i = 3
  while i * i <= n: 
    if n % i == 0: 
      return False
    i += 2
  return True


for num in range(0,200):  # 迭代 10 到 20 之间的数字
    if(isPrime(num)):
     print(num)
