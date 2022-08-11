# 1. 리스트에 넣어서

import sys

sys.stdin=open("sum_input.txt",'r')

def list_max(a):                            #최댓값을 리턴하는 함수 정의
    maxnum=a[0]
    for num in a:
        if num>maxnum:
            maxnum=num
    
    return maxnum

for test_case in range(1, 11):
    T=int(input())
    mat=[list(map(int,input().split())) for _ in range(100)]
    sumlist=[]                              #각 햏,열,대각선의 합을 저장할 리스트          

    for i in range(100):                    #각 행별 합을 리스트에 추가할 거야                  
        horsum=0
        for j in range(100):
            horsum+=mat[i][j]
            sumlist.append(horsum)                                                         
    for j in range(100):                    #각 열별 합을 리스트에 추가할거야                 
        versum=0
        for i in range(100):
            versum+=mat[i][j]
            sumlist.append(versum)                                                         
    rdiagsum=0                              #왼쪽에서 오른쪽으로 가는 대각선에 있는 수들의 합을 추가할 거야        
    for i in range(100):
        for j in range(100):
            if i==j:                        #i==j                                    
                rdiagsum+=mat[i][j]
                sumlist.append(rdiagsum)                                                    
    ldiagsum=0                                     
    for i in range(100):                    #오른쪽에서 왼쪽으로 가는 대각선에 있는 수들의 합을 추가할 거야                 
        for j in range(100):
            if i+j==99:                     #i+j==99
                ldiagsum+=mat[i][j]
                sumlist.append(ldiagsum)                                                    
    print(f'#{T} {list_max(sumlist)}')



# 2. 직접 비교
                                     

#for test_case in range(1, 11+1):
#    T=int(input())
#    mat=[list(map(int,input().split())) for _ in range(100)]
#
#    maxsum=0                                                                #최댓값을 저장할 변수
#
#    for i in range(100):                       
#        horsum=0                                                            # 행 하나의 합을 저장할 함수. 행 하나마다 초기화 시켜 줄 것이다.
#        for j in range(100):                                                # 행 하나를 다 더한다.
#            horsum+=mat[i][j]
#        
#        if horsum>maxsum:                                                   # 그 값이 maxsum보다 크면 maxsum에 저장
#            maxsum=horsum
#
#                                         
#    for j in range(100):
#        versum=0                                                            # 열 하나의 합을 저장할 함수. 행 하나마다 초기화 시켜 줄 것이다.
#        for i in range(100):                                                # 열 하나를 다 더한다.
#            versum+=mat[i][j]
#
#        if versum>maxsum:                                                   # 그 값이 maxsum보다 크면 maxsum에 저장
#            maxsum=versum
#
#
#                                         
#    rdiagsum=0                                                              # 왼쪽에서 오른쪽으로 가는 대각선에 있는 수들의 합을 저장할 변수
#    for i in range(100):
#        for j in range(100):
#            if i==j:                                                        # i==j 대각선 위에 있으면 더한다.
#                rdiagsum+=mat[i][j]
#    if rdiagsum>maxsum:                             
#        maxsum=rdiagsum                                                     # 그 값이 maxsum보다 크면 maxsum에 저장
#
#                                         
#    ldiagsum=0                                                              # 오른쪽에서 왼쪽으로 가는 대각선에 있는 수들의 합을 저장할 변수
#    for i in range(100):                  
#        for j in range(100):
#            if i+j==99:                                                     # i+j==99인 대각선 위에 있으면 더한다.
#                ldiagsum+=mat[i][j]
#    
#    if ldiagsum>maxsum:                                                     # 그 값이 maxsum보다 크면 maxsum에 저장
#        maxsum=ldiagsum
#
#                                         
#    print(f'#{test_case} {maxsum}')