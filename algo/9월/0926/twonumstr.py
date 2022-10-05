T = int(input())

for t in range(1,T+1):
    lena,lenb = map(int,input().split())            # 입력 받는다
    alist=list(map(int,input().split()))
    blist=list(map(int,input().split()))
    mx=0                                            # 촤대값을 저장할 변수

    if lenb>lena:                                   # A가 B보다 짧으면
        for sidx in range(lenb-lena+1):
            numsum=0                                # 곱의 합을 저장할 변수. sidx에 대해 매번 초기화
            for idx in range(lena):
                numsum+=alist[idx]*blist[sidx+idx]  # 곱을 합해줌

            if numsum>mx:                           # 여태까지 mx보다 크면 교체
                mx=numsum

    elif lena>lenb:                                 # A가 길면
        for sidx in range(lena-lenb+1):             # A애 맞춰 옮겨다닌다.
            numsum=0
            for idx in range(lenb):
                numsum+=alist[sidx+idx]*blist[idx]

            if numsum>mx:
                mx=numsum
    
    else:                                           # 길이가 같으면
        numsum=0
        for idx in range(lena):     
            numsum+=alist[idx]*blist[idx]           # 그냥 곱해서 더해줌
        mx=numsum

    print(f'#{t} {mx}')
