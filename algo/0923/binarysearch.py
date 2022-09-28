#def inorder(num):           # 중위순위
#    global cnt
#    if num <= N:            # 숫자가 N보다 작을 때
#        inorder(num*2)      # 왼쪽 자식을 루트로 해서 중위 순위
#        tree[num]=cnt       # 자기 자신의 숫자 저장
#        cnt+=1              # 숫자+1
#        inorder(num*2+1)    # 오른쪽 자식을 루트로 해서 중위 순위
#
#T= int(input())
#
#for t in range(1,T+1):
#    N=int(input())
#    tree=[0]*(N+1)
#    cnt=1
#    inorder(1)
#    
#    print(tree)
def inorder(s):
    global tree
    if s:
        inorder(ch1[s])
        tree.append(s)
        inorder(ch2[s])


T = int(input())

for t in range(1,T+1):
    N=int(input())
    tree=[]                 # 중위 탐색 순서를 저장할 노드
    ch1=[0]*(N+1)
    ch2=[0]*(N+1)
    for n in range(1,N+1):
        if 2*n<= N:
            ch1[n]=2*n
        if (2*n)+1 <= N:
            ch2[n]=(2*n)+1

    inorder(1)

    ans=[0]*(N+1)
    num=1
    for i in tree:
        ans[i]=num
        num+=1
    print(ans)
    print(ans[1],ans[N//2])