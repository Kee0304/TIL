import sys
sys.stdin=open('input.txt')

def inorder(root):
    if int(ch1[root])!=0:                       # 만약 자식이 있으면
        inorder(int(ch1[root]))                 # 왼쪽 서브 트리 재귀
        result.append(par[root][1])             # 알파벳 추가
        inorder(int(ch2[root]))                 # 오른쪽 서브 트리 재귀
    else:
        if type(par[root])==list:               # 타입이 리스트일 때만
            result.append(par[root][1])         # 알파벳 추가

    return result

for t in range(1, 11):
    node=int(input())
    par=[0]*(node+1)                            # 부모
    ch1=[0]*(node+1)                            # 왼쪽 자식
    ch2=[0]*(node+1)                            # 오른쪽 자식
    anlist=[[]*(node+1)]                        # 들어오는 길이가 일정하지 않으므로 일단 리스트로 저장할 거다.
    for _ in range(node):
        anlist.append(list(input().split()))    # 들어오는 놈들을 리스트로 바꿔서 저장해줌
    
    for i in range(1,node+1):
        if len(anlist[i])==4:                   # 만약 들어온 놈의 길이가 4. 즉, 자식이 둘이면
            par[i]=[anlist[i][0],anlist[i][1]]  # 부모 추가
            ch1[i]=anlist[i][2]                 # 왼쪽 자식 추가
            ch2[i]=anlist[i][3]                 # 오른쪽 자식 추가
        elif len(anlist[i])==3:
            par[i]=[anlist[i][0],anlist[i][1]]
            ch1[i]=anlist[i][2]
        elif len(anlist[i])==2:
            par[i]=[anlist[i][0],anlist[i][1]]
    
    result=[]                                   # 결과를 저장할 리스트
    k=inorder(1)                                # root는 모든 테스트 케이스에서 1                         
    print(f'#{t} {"".join(k)}')                 # 리스느 형태이므로 문자열로 합쳐주고 지정된 형식대로 출력