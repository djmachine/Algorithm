def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
        
    toK = ""
    cnt = 0
    
    while(n != 0):
        toK = str(n % k) + toK
        n = n // k
    
    lis = toK.split("0")
    
    for i in lis:
        if i.isdigit() and int(i) != 1 and isPrime(int(i)):
            cnt += 1
    
    return cnt

print(solution(437674, 3))