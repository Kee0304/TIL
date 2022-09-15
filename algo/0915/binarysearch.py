T=int(input())
def inorder(node):             # 노드 번호를 중위 순회를 통해 나열한다.
    global tree
    if node:
        inorder(ch1[node])
        tree.append(node)      # 중위 순회를 통해 나온 노드 번호를 tree 리스트에 append해서 완성.
        inorder(ch2[node])

for t in range(1,T+1):
    N=int(input())
    tree=[]
    ans=[0]*(N+1)
    ch1=[0]*(N+1)
    ch2=[0]*(N+1)

    for n in range(1, N+1):
        if 2*n<=N:              # N노드 보다 2n(왼쪽자식)노드가 작다면
            ch1[n]=2*n          # 왼쪽 자식에 2n을 넣는다.
        if 2*n+1<=N:            # N노드보다 2n+1노드(오른쪽 자식) 노드가 작다면
            ch2[n]=2*n+1        # 오른쪽 자식에 2*n+1을 넣는다.

    inorder(1)                  # root의 노드 번호가 1. root부터 중위 순회 한 노드 번호
    
    q = 1                       # 1씩 늘어나는 자연수
    for e in tree:              # 중위 순회로 나열된 노드 번호들에 대해
        ans[e] = q              # 해당 번호에 차례대로 1씩 늘어나는 자연수를 넣어준다.
        q += 1

    print(f'#{t} {ans[1]} {ans[N//2]}')