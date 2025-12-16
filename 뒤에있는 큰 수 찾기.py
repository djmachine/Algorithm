def solution(numbers):
    
    answer = []
    stack = []
    
    for i in range(len(numbers)-1,-1,-1):
        if not stack:
            answer.append(-1)
            stack.append(numbers[i])
        else:
            for j in range(len(stack)-1,-1,-1):
                if stack[j] > numbers[i]:
                    stack.append(numbers[i])
                    answer.append(stack[j])
                    break    
                else:
                    stack.pop()   
            if not stack:
                answer.append(-1)
                stack.append(numbers[i])

    answer.reverse()
        
    return answer 

print(solution([2, 3, 3, 5]))