import sys

sys.stdin=open("input.txt",'r')

for _ in range(1, 11):                                           # 테스트 케이스는 10개다.
    T=int(input())
    mat=[([0]+list(map(int,input().split()))+[0]) for _ in range(100)]     # 받은 놈들을 매트릭스로 변환할 거다. 그런데, 양 끝에 더미를 넣을 거다.
    
    c_row=99                                                     # 도착지점의 행은 99행. 앞으로 이 변수를 현재 행으로 사용
    c_col=0
    for j in range(102):                                         # 더미를 더해줬으므로, range를 2 늘려서 탐색
        if mat[99][j]==2:
            c_col=j                                              # 도착지점의 열은 값이 2인 열. 앞으로 이 변수를 현재 열로 사용

    old_col=None                                                 # 이전 열을 저장할 변수. 이 놈과 현재 열(c_col)을 비교해서 진행방향을 알아낼 것이다.

    while c_row>-1:
        if mat[c_row][c_col-1]==1 and mat[c_row][c_col+1]==0:    # 만약 현재 위치 기준 왼쪽이 1, 오른쪽이 0인데

            if old_col==None:                                    # old_col이 None 얘는 밑에서 올라온 놈이라는 뜻이므로
                old_col=c_col                                    # old_col에 c_col을 저장하고
                c_col-=1                                         # c_col은 -1 해준다.(왼쪽으로 한 칸 이동한다.)

            elif old_col<c_col:                                  # 만약 old_col<c_col이라면 나는 오른쪽으로 가던 중 0을 만났다는 것이므로
                c_row-=1                                         # 위로 한 칸 이동하고
                old_col=None                                     # old_col은 None으로 되돌린다.

        elif mat[c_row][c_col-1]==1 and mat[c_row][c_col+1]==1:  # 만약 현재 위치 기준 왼쪽이 1, 오른쪽이 1이고

            if old_col<c_col:                                    # old_col<c_col이면 얘는 오른쪽으로 가던 중이었으므로
                old_col=c_col                                    # old_col에 c_col을 저장하고 
                c_col+=1                                         # 오른쪽으로 한 칸 이동한다.

            elif old_col>c_col:                                  # old_col>c_col이면 얘는 왼쪽으로 가던 중이었으므로
                old_col=c_col                                    # old_col에 c_col을 저장하고
                c_col-=1                                         # 왼쪽으로 한 칸 이동한다.

        elif mat[c_row][c_col-1]==0 and mat[c_row][c_col+1]==1:  # 만약 현재 위치 기준 왼쪽이 0, 오른쪽이 1인데

            if old_col==None:                                    # old_col이 None 얘는 밑에서 올라온 놈이라는 뜻이므로
                old_col=c_col                                    # old_col에 c_col을 저장하고
                c_col+=1                                         # c_col은 +1 해준다.(오른쪽으로 한 칸 이동한다.)

            elif old_col>c_col:                                  # 만약 old_col>c_col이라면 나는 왼쪽으로 가던 중 0을 만났다는 것이므로
                c_row-=1                                         # 위로 한 칸 이동하고
                old_col=None                                     # old_col은 None으로 되돌린다.

        else:
            c_row-=1                                             # 양쪽이 0일 때에는 그냥 위로 한 칸씩 올라간다.


                     
                                                                                            
    print(f'#{T} {c_col-1}')                                     # 양 끝에 더미를 넣었으므로, -1을 해주어야 한다.



# 이 외에도 자주 쓰이는 방법으로 지나온 길 지우기, 새로운 2차원 배열 혹은 set에 이미 지났던 길 저장하는 방법 등등이 있다.