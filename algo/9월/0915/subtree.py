def subtree_node(sub_root):         # 서브 노드 개수를 찾는 함수
    global cnt
    if ch1[sub_root]!=0:            # 왼쪽 자식이 존재하면
        print(f'ch1[{sub_root}]={ch1[sub_root]}')
        cnt+=1                      # 개수에 1을 더하고
        subtree_node(ch1[sub_root]) # 왼쪽 서브트리 탐색
    
    if ch2[sub_root]!=0:            # 오른쪽 자식에 대해서도 똑같은 함수 수행 
        print(f'ch2[{sub_root}]={ch2[sub_root]}')
        cnt+=1
        subtree_node(ch2[sub_root])

    return cnt
    


T=int(input())

for t in range(1,T+1):
    E,N=map(int,input().split())
    par=list(range(E+2))                                        # 부모(노드 번호는 E+1까지 존재한다.)
    ch1=[0]*(E+2)                                               # 왼쪽자식
    ch2=[0]*(E+2)                                               # 오른쪽 자식
    nodeinputlist=[0]+list(map(int,input().split()))
    print(nodeinputlist)    

    for idx in range(0,E):                                      # 노드
        if ch1[nodeinputlist[2*idx+1]]==0:                      # 부모 노드(홀수)에 대해 왼쪽 자식이 아직 들어있지 않으면
            ch1[nodeinputlist[2*idx+1]]=nodeinputlist[2*idx+2]  # 왼쪽 자식 추가
        else:
            ch2[nodeinputlist[2*idx+1]]=nodeinputlist[2*idx+2]  # 왼쪽 자식이 이미 있으면 오른쪽 자식 추가


    cnt=1                                                       # 노드 개수를 저장할 변수

    print(f'#{t} {subtree_node(N)}')