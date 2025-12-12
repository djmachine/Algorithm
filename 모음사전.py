def addWord(arr, word, deep):
    if deep == 5:
        return
    lis = ["A", "E", "I", "O", "U"]
    
    for add_word in lis:
        n_word = word + add_word
        arr.append(n_word)
        addWord(arr, n_word, deep+1)
    
    return


def solution(word):
    lis = []
    addWord(lis, "", 0)
    
    for i in range(len(lis)):
        if lis[i] == word:
            answer = i+1 

    return answer 

print(solution("AAUIE"))