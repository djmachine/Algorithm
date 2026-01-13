from collections import deque

def solution(x, y, n):
    
    q = deque()
    dist = [-1] * (y+1)
    dist[x] = 0
    q.append(x)
    
    while(q):
        num = q.popleft()
        if num == y:
            return dist[num]
        
        if num * 2 <= y and dist[num*2] == -1:
            dist[num*2] = dist[num] + 1
            q.append(num*2)
        if num * 3 <= y and dist[num*3] == -1:
            dist[num*3] = dist[num] + 1   
            q.append(num*3)
        if num + n <= y and dist[num+n] == -1:
            dist[num+n] = dist[num] + 1
            q.append(num+n)
        
    return -1

print(solution(10,40,5))