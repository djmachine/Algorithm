from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    visited = [[False] * len(maps[0]) for _ in maps]
    
    q = deque()
    visited[0][0] = True
    q.append((0,0,1))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y, dist = q.popleft()
        
        if x == m-1 and y == n-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1))
    
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))