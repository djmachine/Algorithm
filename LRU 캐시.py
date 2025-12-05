from collections import deque

def solution(c, ci):
    if c == 0:
        return len(ci) * 5
    
    q = deque()
    answer = 0
    
    for i in ci:
        if len(q) < c and i.upper() not in q:
            q.appendleft(i.upper())
            answer += 5
        else:
            if i.upper() in q:
                answer += 1
                q.remove(i.upper())
                q.appendleft(i.upper())
            else:
                answer += 5
                q.pop()
                q.appendleft(i.upper())
                
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))