def permu(i,r):
    global perm
    if i == r:
        tmp=bit[:]
        perm.append(tmp)
        return
    else:
        for n in arr:
            if n not in bit:
                for idx in range(i):
                    if abs(n-bit[idx])==abs(i-idx):
                        break
                else:
                    bit[i]=n
                    permu(i+1,r)
                    bit[i]=None

T=int(input())

for t in range(1,T+1):
    N = int(input())
    arr=list(range(1,N+1))
    bit=[0]*N
    perm=[]
    permu(0,N)
    print(perm)
    print(len(perm))
