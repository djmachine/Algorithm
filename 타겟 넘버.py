from collections import deque

def solution(numbers, target):
    
    cnt = 0
    answer_list = deque()
    answer_list.append(0)
    
    for i in numbers:
        for _ in range(len(answer_list)):
            num = answer_list.popleft()
            answer_list.append(num+i)
            answer_list.append(num-i)
    
    for i in answer_list:
        if i == target:
            cnt+=1
    
    return cnt

print(solution([1, 1, 1, 1, 1],3))