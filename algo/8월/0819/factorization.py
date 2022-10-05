T= int(input())

def eleven(a, cnt):                     # 각 수에 대해 나누어 떨어질 때마다 그 승을 1씩 올리는 함수 들
    while a%11==0:                      # a가 11로 나누어 떨어지는 동안은 계속 반복한다.
        cnt+=1                          # 승을 1 올리고
        a=a/11                          # 11로 나누어준 수로 바꿔줌
    
    return cnt                          # 승을 반환
    

def seven(a,cnt):
    while a%7==0:
        cnt+=1
        a=a/7
    
    return cnt

def five(a,cnt):
    while a%5==0:
        cnt+=1
        a=a/5
    
    return cnt

def three(a, cnt):
    while a%3==0:
        cnt+=1
        a=a/3
    
    return cnt

def two(a, cnt):
    while a%2==0:
        cnt+=1
        a=a/2
    
    return cnt

for t in range(1,T+1):
    N=int(input())
    A=two(N,0)
    B=three(N,0)
    C=five(N,0)
    D=seven(N,0)
    E=eleven(N,0)
    result=map(str,[A,B,C,D,E])
 
    print(f'#{t} {" ".join(result)}')