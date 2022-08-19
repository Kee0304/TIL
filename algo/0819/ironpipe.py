import sys
sys.stdin=open('sample_input.txt')

T=int(input())

for t in range(1,T+1):
    stack=[]
    parenthese=input()
    a=list(parenthese.split('()'))
    
    cnt=0
    sumnum=0
    for k in a:
        if '(' in k:
            sumnum+=k.count('(')
        elif ')' in k:
            cnt+=k.count(')')
            sumnum-=k.count(')')
        elif k=='':
            cnt+=sumnum
    
    print(cnt)
