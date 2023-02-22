def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    
    alphabet = []
    
    for first in words:
        w = first
        alphabet.append(w)
        for second in words:
            w += second
            alphabet.append(w)
            for third in words:
                w += third
                alphabet.append(w)
                for fourth in words:
                    w += fourth
                    alphabet.append(w)
                    for fifth in words:
                        w += fifth
                        alphabet.append(w)
                        w = w[:-1]
                    w = w[:-1]
                w = w[:-1]
            w = w[:-1]
        w = w[:-1]
    
    result = alphabet.index(word)
    result += 1
    
    return result