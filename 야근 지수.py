import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = [-w for w in works]
    heapq.heapify(heap)

    for _ in range(n):
        x = -heapq.heappop(heap)   
        x -= 1
        heapq.heappush(heap, -x)

    answer = 0
    
    for i in heap:
        answer = answer + (i*i)
        
    return answer

print(solution(4,[4, 3, 3]))