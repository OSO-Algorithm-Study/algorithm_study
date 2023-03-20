# 답안 참고 : https://engineer-jjini.tistory.com/283 
# [0]은 내림차순 / [1]은 오름차순
# [0]이 내림차순이므로 [1]이 그 전 수보다 크거나 같아야 검토를 할 필요가 있고, 작으면 둘 다 작다는 의미이므로 skip

def solution(scores):
    wanho = scores[0]
    answer = 1
    scores.sort(key = lambda x : (-x[0], x[1]))
    before = 0
    
    for score in scores:
        if score[0] > wanho[0] and score[1] > wanho[1]:
            return -1
        if before <= score[1]:    
            if score[0] + score[1] > wanho[0] + wanho[1]:
                answer += 1
            before = score[1]
    
    return answer