function solution(scores) {
    var answer = 1;
    const wanho = scores[0];

    scores.sort((a, b) => {
        if (a[0] == b[0]) {
            return a[1] - b[1];
        }
        return b[0] - a[0]});
    
    let before = 0;
    for (const score of scores) {
        if (wanho[0] < score[0] && wanho[1] < score[1]) {
            return -1;
        }
        if (before <= score[1]) {
            if (wanho[0] + wanho[1] < score[0] + score[1]) {
                answer += 1;
            }
            before = score[1];
        }
    }
    return answer;
}