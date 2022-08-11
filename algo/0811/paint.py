from pprint import pprint
import sys

sys.stdin=open("sample_input.txt",'r')

T=int(input())

for t in range(1, T+1):
    N=int(input())                                          # 칠 할 영역의 개수
    paint_list=[]                                           # 입력되는 칠할 영역들을 리스트로 변환해서 리스트로 변환할 거다.
    for _ in range(N):
        paint_list.append(list(map(int,input().split())))

    mat=[["" for _ in range(10)] for _ in range(10)]         # 칠 할 영역을 비어있는 매트릭스로 표현

    for paint in paint_list:
        for i in range(paint[0],paint[2]+1):                 # 주어진 범위 만큼을
            for j in range(paint[1],paint[3]+1):
                mat[i][j]=mat[i][j]+str(paint[4])            # 각 색으로 칠한다.

    cnt=0                                                    # 보라색의 수를 저장할 변수

    for i in range(0,10):                                    # 임의의 요소에
        for j in range(0,10):
            if ('1' in mat[i][j]) and ('2' in mat[i][j]):    # 색1과 색2가 동시에 존재하면
                cnt+=1                                       # 1씩 늘린다.


    print(f'#{t} {cnt}')