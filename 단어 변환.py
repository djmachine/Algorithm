from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    idx = 0
    q = deque()
    q.append([begin, idx])
    
    while(q):
        w, x =  q.popleft()
        if w == target:
            return x
        else:
            for i in range(len(w)):
                for j in words[:]:
                    if w[:i] + w[i+1:] == j[:i] + j[i+1:]:
                        words.remove(j)
                        q.append([j, x+1])

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))