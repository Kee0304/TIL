def BFS(ad,s):
    q=[]
    visited=[]

    q.append(s)
    visited.append(s)

    while 1:
        if q[0] in ad:
            for adj in ad[q[0]]:
                if adj not in visited:
                    q.append(adj)
                    visited.append(adj)
            q.pop(0)

        else:
            return q
            
for t in range(1,11):
    length, sp=map(int,input().split())
    datalist=list(map(int,input().split()))
    adjdict={}
    for idx in range(0,23,2):
        if adjdict.get(datalist[idx])==None:
            adjdict[datalist[idx]]=[datalist[idx+1]]
        else:
            adjdict[datalist[idx]].append(datalist[idx+1])

    h=BFS(adjdict,sp)
    print(f'#{t} {max(h)}')
