def mergesort(lst):                             # 병합 정렬
    if len(lst) == 1:                           # 길이가 1이면
        return lst                              # 그냥 반환
    
    middle=len(lst)//2                          # 중앙 선택

    left=lst[:middle]                           # 중앙을 기준으로 반갈죽
    right=lst[middle:]

    left = mergesort(left)                      # 왼쪽에 대해서 다시 병합정렬
    right = mergesort(right)                    # 오른쪽에 대해서 다시 병합정렬

    return merge(left, right)                   # 병합을 한 놈을 반환

def merge(left, right):                         # 병합 과정
    global cnt                                  # 경우의 수를 셀 변수를 global로 가져옴
    if left[-1]>right[-1]:                      # 만약 오른쪽 리스트가 먼저 없어질 거 같으면
        cnt+=1                                  # 회수 +=1
    result=[None]*(len(left+right))                                   # 병합 결과를 저장할 리스트
    lidx=0
    ridx=0
    idx=0
    while lidx<=(len(left)-1) or ridx<=(len(right)-1):
        if lidx<=(len(left)-1) and ridx<=(len(right)-1):
            if left[lidx]<=right[ridx]:
                result[idx]=(left[lidx])
                idx+=1
                lidx+=1
            else:
                result[idx]=(right[ridx])
                idx+=1
                ridx+=1

        elif lidx<=(len(left)-1) and ridx>=len(right):
            for subidx in range(idx,len(left+right)):
                result[subidx]=left[lidx]
                lidx+=1
            break
        elif ridx<=(len(right)-1) and lidx>=len(left):
            for subidx in range(idx,len(left+right)):
                result[subidx]=right[ridx]
                ridx+=1
            break
    #while left or right:                        # 왼쪽 오른쪽이 아직 비어있지 않을 때
    #    if left and right:                      # 둘 다 비어있지 않으면
    #        if left[0]<=right[0]:               # 만약 오른쪽 첫번째가 더 크면
    #            result.append(left.pop(0))      # 왼쪽 첫번째를 pop해서 결과에 append
    #        else:                               # 왼쪽 첫번째가 더 크면
    #            result.append(right.pop(0))     # 오른쪽 첫번째를 pop해서 결과에 append
    #    elif left:                              # 만약 오른쪽만 비었으면
    #        result.extend(left)                 # 남은 왼쪽 왕창 결과에 extend
    #        break                               # break
    #    
    #    elif right:                             # 만약 왼쪽이 비었으면
    #        result.extend(right)                # 남은 오른쪽 왕창 결과에 extend
    #        break                               # break
    
    return result                               # 병합 결과를 반환

T = int(input())

for t in range(1,T+1):
    N=int(input())
    inlst=list(map(int,input().split()))
    cnt=0
    res=mergesort(inlst)

    print(f'#{t} {res[N//2]} {cnt}')