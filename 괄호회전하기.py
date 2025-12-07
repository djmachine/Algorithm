def check(lis):
    stack = []
    
    for i in lis:
        if len(stack) == 0:
            stack.append(i)
        else: 
            if i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)

            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)

            elif i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(i)

            else:
                stack.append(i)
                
    return False if stack else True

def solution(s):
    
    cnt = 0
    
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            cnt += 1

    
    return cnt