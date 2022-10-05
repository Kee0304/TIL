def Pascal(N):
    pascalN=[[0]*i for i in range(1,N+1)]   # 2차원 배열을 생성한다.
    step=1                                  # 현재 단계를 저장할 정수
    
    while step<=N:                          # 아래에서 위로, tabulation 방식을 사용하겠다.
        if step==1:                         # 첫 줄은 [1]
            pascalN[step-1][0]=1
            step+=1                         # 단계 +1

        elif step==2:                       # 두번째 줄은 [1, 1]
            pascalN[step-1][0]=1
            pascalN[step-1][1]=1
            step+=1                         # 단계 +1

        elif step>=3:
            pascalN[step-1][0]=1            # 각 줄의 처음과
            pascalN[step-1][step-1]=1       # 마지막은 항상 1이다.

            # 파스칼의 삼각형에서, 세번째 줄부터 양끝을 제외한 수는
            # 그 전 단계에서 같은 인덱스의 수와 그 전 인덱스에 있는 수의 합이다.
            for i in range(1,step-1):
                pascalN[step-1][i]=pascalN[step-2][i-1]+pascalN[step-2][i]
            step+=1                         # 단계 +1
    
    return pascalN                          # 저장된 2차원 배열을 반환한다.


T=int(input())
for t in range(1,T+1):
    N=int(input())
    pascal_arr=Pascal(N)                    # N을 입력받아 그에 대한 파스칼 삼각형을 저장한 2차원 배열을 만든다.

    print(f'#{t}')
    # 2차원 배열의 각 요소에 접근해 요소 안의 원소들을 문자열로 바꿔주고,
    # 띄어쓰기를 기준으로 합쳐서 한 줄로 만들어 준 뒤 출력해준다.
    for row in range(0,N):
        print(" ".join(map(str,pascal_arr[row])))    

