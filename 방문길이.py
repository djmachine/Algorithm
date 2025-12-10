def solution(dirs):
    
    cnt = 0
    visited = []
    now = [0,0]
    
    for i in dirs:
        if i == "U":
            nex = [now[0], now[1]+1]
            if now[1]+1 <= 5:
                if [now, nex] not in visited and [nex, now] not in visited:
                    cnt += 1
                    visited.append([now, nex])
                now = nex
                    
        elif i == "D":
            nex = [now[0], now[1]-1]
            if now[1]-1 >= -5:
                if [now, nex] not in visited and [nex, now] not in visited:
                    cnt += 1
                    visited.append([now, nex])
                now = nex

        elif i == "R":
            nex = [now[0]+1, now[1]]
            if now[0]+1 <= 5:
                if [now, nex] not in visited and [nex, now] not in visited:
                    cnt += 1
                    visited.append([now, nex])
                now = nex

                       
        elif i == "L": 
            nex = [now[0]-1, now[1]]
            if now[0]-1 >= -5:
                if [now, nex] not in visited and [nex, now] not in visited:
                    cnt += 1
                    visited.append([now, nex])
                now = nex
    
    return cnt

print(solution("LURDRDUUL"))