from re import sub
import sys
sys.stdin=open('input.txt')

for t in range(1,11):
    N = int(input())
    mat=[]
    for _ in range(N):
        mat.append(list(map(int,input().split())))
    
    cnt=0                                                   # 교착 상태의 수를 저장할 변수

    for col in range(N):
        row=N-1                                             # 열을 기준으로 아래 행에서부터 탐색 시작.
        while row>-1:                                          
            if mat[row][col]==2:                            # 푸른 자성체가 발견되면
                subrow=row-1                                # 바로 위에서부터 붉은 자성체를 찾는다.

                while subrow>-1:                            # 열 0까지 가면 끝낸다.
                    if mat[subrow][col]!=1:                 # 붉은 자성체가 없으면 위를 탐색
                        subrow-=1
                    else:                             
                        cnt+=1                              # 붉은 자성체를 찾으면 교착+=1
                        row=subrow-1                        # 그 아래에 푸른 자성체가 몇 개 있든지 교착은 1개이므로, 그 위부터 다시 탐색한다.
                        break
                else:                                       # subrow가 -1이하가 되면 붉은 자성체를 찾지 못했다는 것으로
                    row-=1                                  # 한 칸 위로 올라간다.

            else:                                           # 푸른 자성체가 없으면 위로 한 칸 올라간다.
                row-=1
    
    print(f'#{t} {cnt}')