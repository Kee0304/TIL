T = int(input())

for t in range(1,T+1):
    busstop=[0]*(5001)
    N=int(input())
    for _ in range(1,N+1):
        A,B=map(int,input().split())
        for idx in range(A,B+1):
            busstop[idx]+=1
    P=int(input())
    ibus=[]
    for _ in range(1,P+1):
        i=int(input())
        ibus.append(busstop[i])
    ibus=list(map(str,ibus))
    busstr=" ".join(ibus)

    print(f'#{t} {busstr}')