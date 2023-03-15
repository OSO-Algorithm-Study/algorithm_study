# 오답이유 : dp는 어차피 지금까지 있었던 것 중에 가장 큰 값을 기억하고 있음
# 연속부분수열 경우를 2가지로 나눠서 dp를 사용하면 최대값을 구할 수 있음 
# 참고한 사이트 : https://velog.io/@dldbdud314/%EC%97%B0%EC%86%8D-%ED%8E%84%EC%8A%A4-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9

def solution(sequence):
    answer = 0    
    seq1 = []
    seq2 = []
    
    if len(sequence) == 1:
        return abs(sequence[0])
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            seq1.append(sequence[i])
            seq2.append(sequence[i] * -1)
        else:
            seq1.append(sequence[i] * -1)
            seq2.append(sequence[i])

    dp1 = [0] * len(sequence)
    dp2 = [0] * len(sequence)
    
    dp1[0] = seq1[0]
    dp2[0] = seq2[0]
    
    for i in range(1, len(sequence)):
        dp1[i] = max(seq1[i], seq1[i] + dp1[i-1])
        dp2[i] = max(seq2[i], seq2[i] + dp2[i-1])
        
        answer = max(answer, abs(dp1[i]), abs(dp2[i]))

    return answer
    
