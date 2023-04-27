function solution(queue1, queue2) {
    var answer = -2;
    
    function sum_queue(queue) {
        let sum = 0;
        for (const element of queue) {
            sum += element;
        }
        return sum;
    }
    
    let tot = 0;
    let sum_queue1 = sum_queue(queue1);
    let sum_queue2 = sum_queue(queue2);
    let max = queue1.length * 3 - 1;
    
    tot = sum_queue1 + sum_queue2;
    
    let cnt = 0;
    let ptr_queue1 = -1;
    let ptr_queue2 = -1;
    
    while(true) {
        
        if (sum_queue1 === sum_queue2 || cnt > max) break;
        
        if (sum_queue1 > sum_queue2) {
            ptr_queue1 += 1;
            let temp = queue1[ptr_queue1];
            queue2.push(temp);
            sum_queue1 -= temp;
            sum_queue2 += temp;
        }
        
        else if (sum_queue1 < sum_queue2) {
            ptr_queue2 += 1;
            let temp = queue2[ptr_queue2];
            queue1.push(temp);
            sum_queue2 -= temp;
            sum_queue1 += temp;
        }
        
        cnt += 1;
    }
    
    if (cnt > max) answer = -1; else answer = cnt;
    
    return answer;
}

// 최대 연산 횟수
// queue1 = [3, 3, 3, 3], queue2 = [3, 3, 3, 21]
// 큐의 길이를 n이라 했을 때, 최대 연산 횟수 = 3 * n - 1