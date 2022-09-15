T=int(input())
for t in range(1, T+1):
    N, M, L = map(int,input().split()) # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    nodelist=[0]*(N+1)
    for _ in range(M):                 # 리스트 형태로 저장
        leaf, num = map(int,input().split())
        nodelist[leaf]=num             # 인덱스에 맞춰 숫자 넣기
 
    for idx in range(N-M,L-1,-1):
        try:                           # 자식 2개를 합하는데
            nodelist[idx]=nodelist[2*idx]+nodelist[2*idx+1]
        except:                        # 자식이 왼쪽 하나면 인덱스 에러가 나므로 except 처리
            nodelist[idx]=nodelist[2*idx]
     
    print(f'#{t} {nodelist[L]}')