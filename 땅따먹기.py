def solution(l):
    
    answer = l[0]
    
    for i in range(1,len(l)):
        a,b,c,d = answer[0], answer[1], answer[2], answer[3]
        
        new_answer = l[i]
        new_answer[0] = new_answer[0] + max(b,c,d)
        new_answer[1] = new_answer[1] + max(a,c,d)
        new_answer[2] = new_answer[2] + max(a,b,d)
        new_answer[3] = new_answer[3] + max(a,b,c)
        
        answer = new_answer

    return max(answer) 

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))