from collections import deque
import sys

sys.stdin = open('sample_input.txt')

def likebfs():
    result=[]
    for num in range(1,node+1):
        if num not in postdict:
            result.append(num)
            visited.add(num)
    
    while 1:
        for _ in range(len(q)):
            front=q.popleft()                           # front에 대해
            if front in adjdict:                        # front에 인접한 정점들이 존재하고
                for adj in adjdict[front]:              # 그 정점들 중에
                    if adj not in visited:              # 방문하지 않은 정점이 있다고 하면
                        if adj in postdict:             # 그 방문하지 않은 정점에 상위 작업이 존재할 때
                            for post in postdict[adj]:  # 그 상위 작업들에 대해
                                if post not in visited: # 끝나지 않은 상위 작업이 하나라도 있으면
                                    break               # 그 정점은 가지 않는다.

                            else:
                                q.append(adj)
                                result.append(adj)
                                visited.add(adj)
        
        if bool(q)==False:
            return result

    

for t in range(1,10+1):
    node, edge = map(int,input().split())
    inlist=list(map(int,input().split()))
    adjdict={}
    postdict={}
    for idx in range(0,len(inlist),2):
        if inlist[idx] in adjdict:
            adjdict[inlist[idx]].append(inlist[idx+1])
        else:
            adjdict[inlist[idx]]=[inlist[idx+1]]

    for idx in range(1,len(inlist),2):
        if inlist[idx] in postdict:
            postdict[inlist[idx]].append(inlist[idx-1])
        else:
            postdict[inlist[idx]]=[inlist[idx-1]]

    visited=set()
    q=deque()
    for num in range(1,node+1):
        if num not in postdict:
            q.append(num)
            visited.add(num)
    
    res=" ".join(list(map(str,likebfs())))

    print(f'#{t} {res}')