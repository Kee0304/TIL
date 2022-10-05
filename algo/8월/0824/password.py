import sys
sys.stdin=open('input.txt')

def password(q):            
    i=1                             # 1~5로 변하며 값에서 빼줄 변수

    # 입력받은 리스트를 queue 처럼 활용할 거다
    while 1:          
        a=q[0]                      # front에 있는 놈을 a에 저장하고    
        del q[0]                    # del을 통해 제거, 자동적으로 앞으로 당긴다.

        if a-i==0 or a-i<0:         # a에서 i를 뺀 놈이 0이거나 0보다 작으면
            q.append(0)             # rear에 0을 넣고
            return q                # 변환된 리스트를 반환한다.

        elif a-i>0:                 # a에서 i를 뺀 놈이 0보다 크면
            q.append(a-i)           # rear에 a-i을 넣고
            if 1<=i<5:              # 만약 i가 1~4라면
                i+=1                # i에 1을 더해주고

            elif i==5:              # 만약 i가 5라면
                i=1                 # 1로 초기화 해준다.

for _ in range(1,11):
    T=int(input())
    plist=list(map(int,input().split()))
    passstr=" ".join(map(str,password(plist)))

    print(f'#{T} {passstr}')