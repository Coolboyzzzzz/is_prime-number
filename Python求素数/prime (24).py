def isprime(a):
 if isinstance(a,int)==False:
  return False
 if a<=1:
  return False
 if a==2:
  return True
 flag=1
 x=int(pow(a,0.5))+1
 for n in range(2,x):
  if a%n == 0:
   flag=0
   break
 if flag==1:
  return True
 else:
  return False

for i in range(2,200): 
  if isprime(i) is True:
      print(i)
