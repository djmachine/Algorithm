def backtraking(k, d, cnt):
    
    max_cnt = cnt
    
    for i, j in enumerate(d):
        if k >= j[0]:
            new_d = d.copy()
            new_d.pop(i)
            
            new_cnt = backtraking(k-j[1], new_d, cnt+1)
            
            max_cnt = max(new_cnt, max_cnt)

    return max_cnt

def solution(k, dungeons):
    
    answer = backtraking(k, dungeons, 0)
    
    return answer


solution([[80,20],[50,40],[30,10]])