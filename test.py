#infix=list('(5+8)*((7+3)/2-3)')
#stack = []
#result = []
#for token in infix:
#
#    if token.isdigit():                                                 # 숫자면
#        result.append(token)                                            # 결과에 push
#
#    else:                                                               # 연산자면
#        if not stack:                                                   # 스택이 비어있으면
#            stack.append(token)                                         # 스택에 push
#
#        else:                                                           # 스택이 차있는데
#            if token == "(":                                            # 여는 괄호면
#                stack.append(token)                                     # 스택에 push
#                print(stack)
#            elif token == ")":                                          # 닫는 괄호면
#                tmp = stack.pop()                                       # pop하는데
#                while tmp != "(":                                       # pop 한 놈이 여는 괄호가 아닌 한
#                    result.append(tmp)                                  # pop 한 놈을 결과에 넣고
#                    tmp = stack.pop()                                   # 다시 stack의 top을 pop                이 경우 pop을 먼저 했으므로 쌍이 맞는 여는 괄호도 스택에서 사라짐
#                    print(stack)
#            elif token == "*" or token == "/":                          # 곱하기나 나누기면
#                while stack and (stack[-1] == "*" or stack[-1] == "/"): # 스택이 차있는데 top이 곱하기나 나누기일 때까지
#                    result.append(stack.pop())                          # pop하고 그 놈을 결과에 넣어줌
#                stack.append(token)                                     # 스탯에 그 곱하기나 나누기인 놈을 넣어줌
#                print(stack)
#            elif token == "+" or token == "-":                          # 더하기나 빼기면
#                while stack and stack[-1] != "(":                       # 스택이 차있고 top이 여는 괄호가 아닌 한
#                    result.append(stack.pop())                          # pop하고 결과에 넣어주고
#                stack.append(token)                                     # 스택에 그 더하기나 빼기인 놈을 넣어줌
#                print(stack)
#for _ in range(len(stack)):                                             # 순회를 마쳤으면
#    result.append(stack.pop())                                          # 스택에 있는 놈들을 하나씩 결과에 넣어준다.
#
#print(result)
a='1     '
print(list(map(int,a.split())))