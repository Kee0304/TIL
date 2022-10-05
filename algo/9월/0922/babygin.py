import sys
sys.stdin = open('sample_input(4).txt','r')

def 트리플렛(cards):                                                             # triplet 판별 함수
    for card in cards:                              
        if cards.count(card)==3:                                            # 돌면서 count 하다가 3개 짜리가 나오면
            return 1                                                        # 1 반환
    else:
        return 0                                                            # for 문이 끝까지 돌면 0 반환

def 런(cards):                                                             # run 판별 함수
    cardsetlist=list(set(cards))                                            # 일단 중복을 제거해줌 (0,1,1,2 와 같은 경우 삭제)
    socards=sorted(cardsetlist)                                             # 정렬해서
    for i in range(len(socards)-2):                                         
        if socards[i]+1==socards[i+1] and socards[i+1]+1==socards[i+2]:     # 연속된 수 3개가 존재하면
            return 1                                                        #  1 반환
    else:
        return 0

def babygin(p1,p2):                                                         # baby gin 판별 함수
    for idx in range(4,12):                                                 # 일단 4개는 미리 넣어놨음
        if idx%2==0:
            p1.append(inlist[idx])                                          # p1에 한 개 먼저 넣고
            if 트리플렛(p1)==1 or 런(p1)==1:                                    # 판별
                return 1                                                    # return
        else:                                                               # p2에 한 개 넣기
            p2.append(inlist[idx])
            if 트리플렛(p2) == 1 or 런(p2) == 1:    
                return 2
    else:
        return 0

T=int(input())

for t in range(1,T+1):
    inlist=list(map(int,input().split()))
    p1=[inlist[0],inlist[2]]
    p2=[inlist[1],inlist[3]]
    
    result=babygin(p1,p2)
    if result == 1:
        print(f'#{t} 1')
    elif result == 2:
        print(f'#{t} 2')
    else:
        print(f'#{t} 0')