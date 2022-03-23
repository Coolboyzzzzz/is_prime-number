l=list(range(2,1000))

for n,i in enumerate(l):
  for j in l[n+1:]:
    if j%i==0:
      l.remove(j)

print(l)
