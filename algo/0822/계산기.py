infix = "(6+5*(2-8)/2)"
stack = []
result = []
for token in infix:

    if token.isdigit():                                                 # 숫자면
        result.append(token)                                            # 결과에 push
                            
    else:                                                               # 연산자면
        if not stack:                                                   # 스택이 비어있으면
            stack.append(token)                                         # 스택에 push
                            
        else:                                                           # 스탯이 차있는데
                                    
            if token == "(":                                            # 여는 괄호면
                stack.append(token)                                     # 스택에 push
                            
            elif token == ")":                                          # 닫는 괄호면
                tmp = stack.pop()                                       # pop하는데
                while tmp != "(":                                       # pop 한 놈이 여는 괄호일 때까지 반복
                    result.append(tmp)                                  # pop 한 놈을 결과에 넣고
                    tmp = stack.pop()                                   # 다시 stack의 top을 pop

            elif token == "*" or token == "/":                          # 곱하기나 나누기면
                while stack and stack[-1] == "*" or stack[-1] == "/":   # 스택이 차있는데 top이 곱하기나 나누기일 때까지
                    result.append(stack.pop())                          # pop하고 그 놈을 결과에 넣어줌
                stack.append(token)                                     # 스탯에 그 곱하기나 나누기인 놈을 넣어줌

            elif token == "+" or token == "-":                          # 더하기나 빼기면
                while stack and stack[-1] != "(":                       # 여는 괄호가 아닐 때까지
                    result.append(stack.pop())                          # pop하고 결과에 넣어주고
                stack.append(token)                                     # 스택에 그 더하기나 빼기인 놈을 넣어줌

for _ in range(len(stack)):
    result.append(stack.pop())


for token in result:
    if token.isdecimal():
        stack.append(int(token))
    else:
        if token == "+":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2+p1)
        elif token == "-":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2-p1)
        elif token == "*":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2*p1)
        elif token == "/":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2/p1)
ans = stack.pop()










