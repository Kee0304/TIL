T= int(input())

def Paper(N):                                   # 재귀함수를 만들어 푼다.
    if N==10:
        return 1                                # 길이가 10이면 당연히 한 번
    elif N==20:
        return 3                                # 길이가 20이면 좌우,상하,정사각형으로 3개
    elif N>=30:
        return 1*Paper(N-10)+2*Paper(N-20)      # 10을 뺐을 때와 20을 뺐을 때에는 사실 중복이 하나

for t in range(1, T+1):
    N=int(input())
    print(f'#{t} {Paper(N)}')