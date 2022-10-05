from pprint import pprint
import sys
sys.stdin=open('sample_input(1).txt')

T = int(input())

for t in range(1,T+1):
    N,M= map(int,input().split())
 
    mat=[]
    for _ in range(0,N):
        mat.append(list(input()))

    if N==M:                                                # 편의를 위해 N==M일 때와 그렇지 않을 때로 나누었다.
        for i in range(N):                                  # 먼저 행에 대해 검사
            stralist=[]                                     # 문자 10개를 저장할 리스트 초기화
            for j in range(N):    
                stralist.append(mat[i][j])                  # 문자열 하나씩 넣어줌
            
            if stralist==stralist[::-1]:                    # 만약 원본이랑 뒤집은 거랑 같게 보이면
                palinlist=stralist                          # 요놈이 회문이다.
                break

        else:
            for j in range(N):                              # 행 탐색에서 회문이 발견되지 않았으면, 열에 대해 탐색
                strblist=[]
                for i in range(N):
                    strblist.append(mat[i][j])
 
                if strblist==strblist[::-1]:
                    palinlist=strblist                      # 행 때와 같은 과정을 거친다.
                    break

        
    else:                                                   # N!=M일 때
        for i in range(N):                                  # 행에서 부터 검사 시작
            for j in range(N-M+1):                          # j의 경우 N-M+1개 번만큼
                strclist=[]                                 # M개를 넣어줄 리스트 초기화
                for k in range(j,j+M):                      # M번 동안
                    strclist.append(mat[i][k])              # 문자를 하나씩 넣어줌

                if strclist==strclist[::-1]:
                    palinlist=strclist
                    break
        
        
        else:
            for j in range(N):                              # 행 탐색에서 회문이 발견되지 않았으면, 열에 대해 탐색
                for i in range(N-M+1):
                    strdlist=[]
                    for k in range(i,i+M):
                        strdlist.append(mat[k][j])

                    if strdlist==strdlist[::-1]:
                        palinlist=strdlist
                        break

    palin=''.join(palinlist)
    print(f'#{t} {palin}')