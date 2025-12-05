def solution(p, l):
    q = []
    idx = 1

    #queue 제작
    for i in range(len(p)):
        if i == l:
            q.append([p[i], 1])
        else:
            q.append([p[i], 0])

    #프로세스 실행
    while(1):
        if q[0][0] != max(q)[0]:
            q.append(q.pop(0))
        else:
            if q[0][1] == 1:
                break
            else:
                q.pop(0)
                idx += 1
    
    return idx

print(solution([2, 1, 3, 2],2))