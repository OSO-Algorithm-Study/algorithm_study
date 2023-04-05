function solution(k, d) {
    var answer = 0;

    for (let i =0; i <= d; i += k){
        let j = (d**2 - i**2)**0.5
        answer += Math.ceil(j / k);
        if (j % k == 0){
            answer += 1;
        }
    }
    
    return answer;
}