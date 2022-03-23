p=[2]
for i in range(2,101):
  for temp in range(2,i):
    if i%temp==0:
      break
      print('i=',i,'temp=',temp)
    elif temp==i-1:
      p.append(i)
print('\n以下打印质数：')
print(p)
