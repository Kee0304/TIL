import sys
sys.stdin=open('sample_input.txt')

T = int(input())

for t in range(1,T+1):
    inp=list(input().split())                       # 입력 받은 문자열을 리스트로 변환

    stack=[]                                        # 이용할 스택

    for idx in range(len(inp)):                     # 인덱스로 탐색
        try:
            if inp[idx].isdecimal() == True:        # 만약 숫자면
                stack.append(int(inp[idx]))         # int로 변환하여 스택에 집어넣는다.

            elif inp[idx]=='+':                     # 다음으로 각각의 연산자에 대하여
                v2=stack.pop()                      # 먼저 pop 한 놈을 v2
                v1=stack.pop()                      # 다음에 pop한 놈을 v1이라 하고
                ans=v1+v2                           # 그 연산 결과는 ans라 한 다음
                stack.append(ans)                   # 스택에 쌓아준다.

            elif inp[idx]=='-':
                v2=stack.pop()
                v1=stack.pop()
                ans=v1-v2
                stack.append(ans)

            elif inp[idx]=='*':
                v2=stack.pop()
                v1=stack.pop()
                ans=v1*v2
                stack.append(ans)

            elif inp[idx]=='/':
                v2=stack.pop()
                v1=stack.pop()
                ans=v1//v2
                stack.append(ans)

            elif inp[idx]=='.':                     # .이 나왔으면
                ans=stack.pop()                     # 스택을 pop해주는데
                if stack:                           # 만약 스택이 차 있으면
                    print(f'#{t} error')            # 식이 잘못 된 것이므로 error 출력
                    break
                else:                               # 스택이 비어있으면
                    print(f'#{t} {ans}')            # ans 출력
                    break

        except:                                     # 각종 에러가 나면 error 출력
            print(f'#{t} error')
            break
