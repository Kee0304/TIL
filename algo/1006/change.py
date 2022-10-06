T = int(input())

for t in range(1,T+1):
    N=int(input())
    par=[50000,10000,5000,1000,500,100,50,10]
    res=[0,0,0,0,0,0,0,0]

    for idx in range(len(par)):
        while N>=par[idx]:
            N-=par[idx]
            res[idx]+=1
    
    resstr = " ".join(map(str,res))
    print(f'#{t}')
    print(resstr)