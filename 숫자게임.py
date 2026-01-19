def solution(A, B):
    
    answer = 0
    A.sort()
    B.sort()
    aidx = 0
    bidx = 0
    
    while(bidx < len(B)):
        if B[bidx] > A[aidx]:
            answer += 1
            aidx += 1
        bidx += 1
            
    return answer

print(solution([5,1,3,7],[1,2,3,4]))