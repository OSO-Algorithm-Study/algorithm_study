function solution(queue1, queue2) {
    let max_cnt = queue1.length * 3;
    let queue1_sum = queue1.reduce((sum, currValue) => {
    return sum + currValue;
    }, 0);
    let queue2_sum = queue2.reduce((sum, currValue) => {
    return sum + currValue;
    }, 0);
    
    let cnt = 0;
    let tmp_elm;
    let [a_idx, b_idx] = [0, 0];
    while (cnt <= max_cnt){
        if (queue1_sum > queue2_sum){
            tmp_elm = queue1[a_idx];
            a_idx++;
            queue2.push(tmp_elm);
            queue1_sum -= tmp_elm;
            queue2_sum += tmp_elm;
            cnt++;
        } else if (queue1_sum < queue2_sum){
            tmp_elm = queue2[b_idx];
            b_idx++;
            queue1.push(tmp_elm);
            queue2_sum -= tmp_elm;
            queue1_sum += tmp_elm;
            cnt++;
        }
        if (queue1_sum == queue2_sum) return cnt;
    }
    return -1;
}