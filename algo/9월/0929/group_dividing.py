def make_set(x):
    parent[x] = x

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union(x,y):
    parent[find_set(y)] = find_set(x)
    

# kruskal

def mst_kruskal():

    mst = []

    for i in range(people+1):
        make_set(i)

    while len(mst) < people and graph_kruskal:
        s, e = graph_kruskal.pop(0)
        if find_set(s) != find_set(e):
            mst.append([s,e])
            if type(graph[find_set(s)]) == int:
                graph[find_set(s)]={(graph[find_set(s)])}
            
            if type(graph[find_set(e)]) == int:
                graph[find_set(s)].add(graph[find_set(e)])
            else:
                graph[find_set(s)].update(graph[find_set(e)])
            
            graph[find_set(e)]=set()

            union(s,e)
    return graph

T = int(input())

for t in range(1,T+1):
    people, paper = map(int,input().split())
    parent = [-1]*(people+1)
    inlist=list(map(int,input().split()))
    graph_kruskal=[]
    for idx in range(0,len(inlist),2):
        graph_kruskal.append(sorted([inlist[idx],inlist[idx+1]]))
    
    graph=list(range(people+1))

    mmsstt=mst_kruskal()

    cnt=0
    for s in mmsstt:
        if s:
            cnt+=1
    
    print(f'#{t} {cnt}')