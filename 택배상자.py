from collections import deque

def solution(order):
    
    q = []
    lis = [i for i in range(len(order), 0, -1)]
    idx = 0
    answer = 0
    n = lis.pop()
    
    while(1):
        if n != 0:
            if n == order[idx]:
                answer += 1
                idx += 1
                if lis:    
                    n = lis.pop()
                else:
                    n = 0

            elif n < order[idx]:
                q.append(n)
                if lis:
                    n = lis.pop()
                else:
                    n = 0

            elif n > order[idx]:
                if q:
                    if q[-1] == order[idx]:
                        answer += 1
                        idx += 1
                        q.pop()
                    elif q[-1] > order[idx]:
                        return answer
                    elif q[-1] < order[idx]:
                        q.append(n)
                else:
                    return answer
        else:
            if q:
                if q[-1] == order[idx]:
                    answer += 1
                    idx += 1
                    q.pop()
                else:
                    return answer
            else:
                return answer
    
    return 

print(solution([4, 3, 1, 2, 5]))