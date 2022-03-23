i=int(input('enter an integer please:'))
b=False
for a in range(2,i):
  for c in range(2,a):
    if a%c==0:
      b=False
      break
    else:
     b=True
  if b == True:
    print (a)
