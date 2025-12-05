def solution(p,s):
    
    p.reverse()
    s.reverse()
    answer = []
    
    while(p):
        for i in range(len(p)):
            p[i] = p[i] + s[i]            
            
        if p and p[-1] >= 100:
            cnt = 0
            while(p and p[-1]>=100):
                p.pop()
                cnt += 1
            answer.append(cnt)
    
    return answer

print(solution([93, 30, 55], [1, 30, 5]))