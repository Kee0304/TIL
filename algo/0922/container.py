import sys
sys.stdin = open('sample_input(2).txt')


T=int(input())

def load(weightlist,capacity):                          # 조건에 따라 짐을 싫는 함수
    truck_load=[]                                       # 실린 짐들의 무게
    for truck_capa in capacity:                         # 적재 용량에 대해 반복
        for idx in range(len(weightlist)):              # 무게에 대해 반목
            if truck_capa == 0:                         # 적재 용량이 0이면
                break                                   # break
            else:                                       # 적재용량이 0이 아닐 때
                if truck_capa >= weight_list[idx]:      # 만약 적재 용량이 무게보다 크면
                    truck_load.append(weight_list[idx]) # 무게 추가
                    truck_capa=0                        # 두 개 이상 적재할 수 없으므로 적재 용량을 0으로
                    weight_list[idx]=99999999999        # 무게는 암의의 큰 수로 하여 적재되었음을 표현

    return truck_load



for t in range(1,T+1):
    N,M=map(int,input().split())
    weight_list=sorted(list(map(int,input().split())), reverse=True)    # 입력을 받고 내림차순으로 정렬
    capa=sorted(list(map(int,input().split())), reverse=True)           # 입력을 받고 내림차순으로 정렬
    result=load(weight_list,capa)                                       # 적재용량이 큰 트럭에 무거운 짐을 적재하는 형식

    print(f'#{t} {sum(result)}')

    