def solution(topping):
    cnt = 0
    t1 = {}
    t2 = {}
    
    for i in topping:
        if i in t2:
            t2[i] += 1
        else:
            t2[i] = 1
            
    for i in topping:
        t1[i] = 1
        t2[i] -= 1
        if t2[i] == 0:
            t2.pop(i)
        
        if len(t1) == len(t2):
            cnt += 1
            
    return cnt 

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))