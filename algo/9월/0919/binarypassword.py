import sys
sys.stdin = open('input.txt')

def bipw(instr):
    pslist=[]                               # 암호코드가 거꾸로 저장될 리스트
    
    for idx in range(len(instr)-1, -1 ,-7): # 뒤에서부터 7개씩 건너 뛰면서 탐색
        if len(pslist)==8:                  # 길이가 8이면 반환
            return pslist
        if instr[idx-6:idx+1]=='0001101':   # 정해진 규칙에 맞춰서 숫자 하나씩 append
            pslist.append(0)
        elif instr[idx-6:idx+1]=='0011001':
            pslist.append(1)
        elif instr[idx-6:idx+1]=='0010011':
            pslist.append(2)
        elif instr[idx-6:idx+1]=='0111101':
            pslist.append(3)
        elif instr[idx-6:idx+1]=='0100011':
            pslist.append(4)
        elif instr[idx-6:idx+1]=='0110001':
            pslist.append(5)
        elif instr[idx-6:idx+1]=='0101111':
            pslist.append(6)
        elif instr[idx-6:idx+1]=='0111011':
            pslist.append(7)
        elif instr[idx-6:idx+1]=='0110111':
            pslist.append(8)
        elif instr[idx-6:idx+1]=='0001011':
            pslist.append(9)
    return pslist                       # 암호 코드가 거꾸로 담긴 리스트 반환

T=int(input())                          # 테스트 케이스

for t in range(1,T+1):                  # 횟수만큼
    N, M=map(int,input().split())       # N,M 입력 받고
    for _ in range(N):                  # N번
        instr=input()                   # 줄을 입력받아서
        if instr=='0'*M:                # 0으로만 되어있으면 패스
            pass
        else:                           # 아니면 psstr=instr
            psstr=instr

    b=psstr.rstrip('0')                 # 오른쪽에 0다 제거
    c=bipw(b)                           # 함수 실행
    a=c[::-1]                           # 뒤집기

    if (((a[0]+a[2]+a[4]+a[6])*3)+(a[1]+a[3]+a[5]+a[7]))%10==0:  # 조건에 맞으면
        print(f'#{t} {a[0]+a[2]+a[4]+a[6]+a[1]+a[3]+a[5]+a[7]}') # 숫자를 다 합쳐서 출력
    else:
        print(f'#{t} 0')                                         # 아니면 0 출력

    
    

                
