T=int(input())

for t in range(1,T+1):
    M=input().strip()
    N=input().strip()   # 각각 입력받고
    if M in N:          # 있으면
        result='1'              # 1
    else:
        result='0'              # 없으면 0

    print(f'#{t} {result}')