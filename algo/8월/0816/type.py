T=int(input())

for t in range(1,T+1):
    A,B = input().split()
    typing=len(A)                               # 타이핑 횟수 변수
    C=A                                         # 문자열은 immutable이므로 깊은 복사 필요 없음
    for i in range(0,len(A)-len(B)+1):          # len(A)-len(B)를 벗어나면 range 밖으로 벗어난다.
        if C[i:i+len(B)]==B:                    # len(B) 길이 만큼 잘라내서 검사하자.
            typing-=(len(B)-1)                  # B와 일치하는 패턴이 발견되면, 한 번은 쳐야 되므로 len(B)-1 만큼 빼준다.
            strclist=list(C)                    # 그 뒤 C를 리스트로 바꾼 후
            for i in range(i,i+len(B)):
                strclist[i]='0'                 # 패턴이 일치했던 부분은 0으로 대체
            C="".join(strclist)                 # 다시 문자열로 합쳐서, 000~~과 같은 형태로 바꾸어 겹치는 상황을 없애준다.

    print(f'#{t} {typing}')