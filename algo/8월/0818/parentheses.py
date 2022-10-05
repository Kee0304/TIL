import sys
sys.stdin=open('sample_input(1).txt')

T=int(input())

def parenth(string):
    strlist=list(string)
    stack=[]
    for i in range(len(strlist)):
        if (strlist[i] == '(') or (strlist[i] == '{'):      # 왼쪽 괄호는 일단 스택에 넣고 본다.
            stack.append(strlist[i])
        
        elif strlist[i] == ')':                             # 닫는 소괄호가 나왔는데

            if stack!=[] and stack[-1]=='(':                # 스택 맨 위가 여는 소괄호면
                stack.pop()                                 # 스택에서 여는 소괄호를 지워준다.

            elif stack==[]:                                 # 만약 스택이 비어있는데 여는 괄호가 나온 것이라면  
                return('0')                                 # 올바른 괄호가 아니다.


            elif stack!=[] and stack[-1]!='(':              # 만약 스택이 비어있는데 닫는 괄호가 나온 것이라면 
                return('0')                                 # 올바른 괄호가 아니다.                
                                       
        

        elif strlist[i] == '}':                             # 닫는 중괄호가 나왔는데

            if stack!=[] and stack[-1]=='{':                # 스택 맨 위가 여는 중괄호면
                stack.pop()                                 # 스택에서 여는 중괄호를 지워준다.

            elif stack==[]:                                 # 만약 스택이 비어있는데 닫는 괄호가 나온 것이라면 
                return('0')                                 # 올바른 괄호가 아니다.


            elif stack!=[] and stack[-1]!='{':              # 만약 스택이 비어있지는 않아도 스택 맨 위가 여는 중괄호가 아니라면
                return('0')                           # 올바른 괄호가 아니다.
    
    else:
        if stack==[]:
            return('1')
        else:
            return('0')


for t in range(1,T+1):
    string=input()
    print(f'#{t} {parenth(string)}')