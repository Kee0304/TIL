import sys
sys.stdin=open('sample_input(1).txt')

def permu(idx , r, temp, accu):             # 순열을 만드는 함수
    global res                              # res 가져옴
    if idx == r:                            # 만약 현재 idx가 원하는 순열 길이 r과 같다면
        last_arrive = temp[-1]              # temp 맨 끝에 있는 놈을 마지막 도착 지점으로 저장하고
        accu += lst[last_arrive-1][0]       # 누적에 마지막 지점에서 사무실로 돌아가는 수를 더해줌
         
        if accu < res:                      # 만약 누적이 여태까지 결과보다 작으면
            res = accu                      # 저장
 
        accu -= lst[last_arrive-1][0]       # 마지막 지점에서 사무실로 오는 만큼을 빼주고
        return                              # 함수 종료
     
    start = temp[-1]                        # 만약 길이가 r이 아니면 시작지점은 temp의 끝
    for i in range(2, n+1):                 # 사무실부터 만들 필요는 없음
        if i not in temp:                   # 만약 temp에 i가 없다면
            temp.append(i)                  # 더해주고
            arrive = temp[-1]               # 도착지점은 temp의 마지막 놈
            energy = lst[start-1][arrive-1] # 소비 전력을 lst에서 찾고
            accu += energy                  # 누적에 더해줌

            if accu > res:                  # 만약 누적이 이미 여태까지 결과보다 크다면
                temp.pop()                  # 더 할 필요가 마지막 방문 지점을 빼고
                accu -= energy              # 소비 전력도 빼주고
                continue                    # 다음 i에 대해 루프 시작

            permu(idx+1, r, temp, accu)     # 누적이 여태까지 결과보다 작다면 인덱스를 하나 올려서 함수 실행

            temp.pop()                      # 현재 하나 올린 함수의 실행이 끝났으면 끝에 하나를 빼주고
            accu -= energy                  # 누적 소비 에너지 역시 빼준다.
 
 
 
T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
 
 
    res = 999999999999999
    permu(1, n, [1], 0)
    print(f'#{case+1} {res}')