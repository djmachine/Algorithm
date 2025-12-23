import heapq

def solution(s, K):
    
    heapq.heapify(s)
    cnt = 0
    
    while(1):
        i = heapq.heappop(s)
        if i >= K:
            break
        if not s:
            return -1
        j = heapq.heappop(s)
        
        num = i + (j*2)
        heapq.heappush(s, num)
        cnt += 1
    
    return cnt


print(solution([1, 2, 3, 9, 10, 12],7))