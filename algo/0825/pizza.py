import sys
sys.stdin=open('sample_input(2).txt')


T=int(input())

def pizza(cheese,pot):                          # 피자를 돌리는 함수
    oven=[]                                     # 화덕 내부 상황 queue

    for _ in range(pot):                        # 일단 화덕 크기 만큼
        a=cheese.pop(0)                         # 피자들의 리스트를 앞에서 부터 하나 꺼내서
        oven.append(a)                          # 화덕 내부에 넣어준다.
    

    while 1:
        oven[0][1]=(oven[0][1])//2              # 치즈를 //2 해주고
        one=oven.pop(0)                         # dequeue 한 뒤
        oven.append(one)                        # 넣어줌

        if oven[-1][1]!=0:                      # front의 치즈가 0이 아니면
            continue                            # 루프를 계속 돈다.

        elif oven[-1][1]==0:                    # front의 치즈가 0인데
            if cheese!=[]:                      # 아직 넣을 피자가 남아있으면
                oven.pop(-1)                    # front를 pop하고
                new=cheese.pop(0)               # 새로운 피자를 하나 꺼내서
                oven.append(new)                # 넣는다.

            elif cheese==[] and len(oven)>2:    # 만약 더 이상 피자가 없고 오븐 내부에 3개 이상의 피자가 있으면
                oven.pop(-1)                    # front를 빼주고 루프를 계속 돌린다.
                
            elif cheese==[] and len(oven)==2:   # 만약 더 이상 피자가 없고 오븐 내부에 피자가 2개라면
                oven.pop(-1)                    # front를 빼주고 
                return oven.pop(0)              # 마지막 남은 놈을 반환해준다.


for t in range(1,T+1):
    N,M=map(int,input().split())
    ci=list(map(int,input().split()))
    cilist=[]
    for i,el in enumerate(ci):
        cilist.append([i+1,el])                 # enumerate를 사용해서 인덱스+1과 치즈를 리스트 형태로 같이 저장


    print(f'#{t} {pizza(cilist,N)[0]}')