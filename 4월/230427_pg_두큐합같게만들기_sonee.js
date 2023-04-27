function solution(queue1, queue2) {
    
    let queue = [...queue1, ...queue2, ...queue1, ...queue2];
    const len = queue1.length + queue2.length
    let count = 0;
    
    let start1 = 0, end1 = len/2 - 1;
    let start2 = len/2 , end2 = len - 1;
    
    let sum1 = queue.slice(start1, end1 + 1).reduce((acc, cur) => acc + cur, 0);
    let sum2 = queue.slice(start2, end2 + 1).reduce((acc, cur) => acc + cur, 0);

    while(sum1 !== sum2) {
        if (sum1 > sum2) {
    
            sum1 -= queue[start1];
            start1 += 1;
            
            sum2 += queue[end2+1];
            end2 += 1;
            
        } else {
            sum1 += queue[end1+1];
            end1 += 1;
            
            sum2 -= queue[start2];
            start2 += 1;
        }

        count++;

        if (count === 2*len) {
            count = -1;
            break;
        }
    }
    return count;
}