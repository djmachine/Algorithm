from collections import deque

def solution(n, computers):
    
    visited = [False for _ in range(n)]
    network = {}
    q = deque()
    network_value = 0
    index = 0
    
    while(False in visited):
        # 아직 네트워크에 가입하지 않은 컴퓨터 찾기
        for i in range(n):
            if visited[i] == False:
                index = i
                break
                
        # 네트워크에 가입시킨후, q에 넣어 넓이 우선탐색 진행
        visited[index] = True
        network[network_value] = [index]
        q.append(index)
        
        # 해당 네트워크의 연결된 컴퓨터들 찾기
        while(q):
            com = q.popleft()
            for i in range(n):
                if computers[com][i] == 1 and visited[i] == False:
                    visited[i] = True
                    q.append(i)
                    network[network_value].append(i)
        
        # 해당번째 네트워크를 찾았으면 다음 네트워크번호 부여
        network_value += 1
    
    return len(network)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))