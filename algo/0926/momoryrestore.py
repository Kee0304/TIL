def chbit(original, tmp, idx, cnt):                 # 메모리를 고치면서 그 회수를 저장하는 함수
    if original == tmp:                             # 만약 바꾼 메모리가 원래와 같다면
        return cnt                                  # 여태까지 바꾼 회수를 반환
    while 1:                                        # 무한 반복
        if original[idx]!=tmp[idx]:                 # idx에 대해 같지 않으면
            cnt+=1                                  # 고친다.
            for subidx in range(idx,len(original)):
                if original[idx] ==1:               # original에 대해 같은 놈으로
                    tmp[subidx]=1                   # 뒤를 전부 바꿔줌
                else:
                    tmp[subidx]=0
            break
        else:
            idx+=1                                  # 같으면 그냥 idx만 한 칸 뒤로
    
    return chbit(original,tmp,idx,cnt)              # 다음 idx와 cnt에 대해 함수 다시 실행

T=int(input())

for t in range(1,T+1):
    original=list(map(int,input()))
    tmp=[0]*len(original)

    result=chbit(original,tmp,0,0)
    
    print(f'#{t} {result}')
    