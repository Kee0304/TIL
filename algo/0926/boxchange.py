T=int(input())

for t in range(1, T+1):
    N,Q = map(int,input().split())
    boxlist=[0]+[0]*N
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for idx in range(L, R+1):
            boxlist[idx]=i
    boxlist.pop(0)
    boxlist=list(map(str,boxlist))
    boxstr=" ".join(boxlist)
    print(f'#{t} {boxstr}')