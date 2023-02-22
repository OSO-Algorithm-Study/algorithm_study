_from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words_size = len(words)
    visited = [0] * words_size
    
    result = bfs(begin, target, words, visited)
    
    return result
    
    
def bfs(begin, target, words, visited):
    q = deque([])
    q.append([begin, 0])
    
    while q:
        elem = q.popleft()
        
        if elem[0] == target:
            return elem[1]
        
        for word in words:
            chk = check_count(elem[0], word)
            if chk == 1 and visited[words.index(word)] == 0:
                q.append([word, elem[1]+1])

    
    return 0
                
def check_count(word1, word2):
    count = len(word1)
    word_size = count
    for i in range(word_size):

        if word1[i] == word2[i]:
            count -= 1

    return count