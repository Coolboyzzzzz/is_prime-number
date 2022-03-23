N=1000 #终止为1000
Primes=[True for k in range(N+1)] 
p=2  #从2开始
Primes[0]=False # 0不是一个可用的
Primes[1]=False #1也是不是可用的
while(p*p<=N):
    if Primes[p]==True: 
        for j in range(p*p,N+1,p): 
            Primes[j]=False 
    p+=1 
for i in range(2,N): 
    if Primes[i]:  #判断是否为素数
        print(i)
