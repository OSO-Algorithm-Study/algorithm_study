function solution(k, ranges) {
    let answer = [];
    const integral = [0];
    
    while (k != 1){
        if (k % 2 == 0){
            integral.push((k + k / 2) / 2 + integral.at(-1));
            k = k / 2;
        } else{
            integral.push((k + (k * 3 + 1)) / 2 + integral.at(-1));
            k = k * 3 + 1;
        }
    }
    for (let [x, y] of ranges){
        if (x > integral.length -1 + y){
            answer.push(-1);
        } else{
            answer.push(integral.at(-1+y) - integral[x]);
        }
    }
    return answer;
}