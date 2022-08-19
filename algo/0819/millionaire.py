import sys
sys.stdin=open('input.txt')

T=int(input())

for t in range(1,T+1):
    daylong=int(input())
    price_list=list(map(int,input().split()))

    std_price=price_list[daylong-1]                     # 일단은 마지막 날 가격을 구입할지 말지 정하는 기준 가격으로 설정
    earn=0                                              # 순이익을 저장할 변수
    for day in range(daylong-1, -1, -1):
        if price_list[day]<std_price:                   # 만약 가격이 기준 가격보다 싸면
            earn+=(std_price)-(price_list[day])         # 그에따른 이익을 더해준다.
        
        elif price_list[day]>std_price:                 # 만약 가격이 기준 가격보다 비싸면
            std_price=price_list[day]                   # 가격을 기준 가격으로 바꾼다.

    print(f'#{t} {earn}')
        