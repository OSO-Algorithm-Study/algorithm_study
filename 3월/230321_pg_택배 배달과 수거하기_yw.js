function solution(cap, n, deliveries, pickups) {
    var answer = 0;
    // solution 1
    // let sumDeliver = sum(deliveries);
    // let sumPick = sum(pickups);
    
    // while (sumDeliver + sumPick !== 0) {
    //     // 배달
    //     let deliverLength = estimateLen(deliveries);
    //     let delCnt = deliverAndRet(deliveries, cap);
    //     // 수거
    //     let pickupLength = estimateLen(pickups);
    //     let retCnt = deliverAndRet(pickups, cap);
            
    //     answer += Math.max(deliverLength, pickupLength) * 2
    //     sumDeliver -= delCnt;
    //     sumPick -= retCnt;
    // }
    // solution 2
    let d = 0;
    let p = 0;
    
    for (let i = n - 1; i >= 0; i--) {
        let cnt = 0;
        
        d -= deliveries[i];
        p -= pickups[i];
        
        while (d < 0 || p < 0) {
            d += cap;
            p += cap;
            cnt += 1;
        }
        
        answer += (i + 1) * 2 * cnt;
    }

    return answer;
}


function sum(array) {
    let result = 0;
    for (const element of array) {
        result += element;
    }
    return result;
}


function estimateLen(array) {        
    for (let i = array.length - 1; i >= 0; i--) {
        if (array[i] === 0) array.pop(); else return array.length;
    }
    return 0;
}


function deliverAndRet(array, cnt) {
    let res = 0;
    for (let i = array.length - 1; i >= 0; i--) {
        if (array[i] < cnt) {
            cnt -= array[i];
            res += array[i];
            array[i] = 0;
        }
        else {
            array[i] -= cnt;
            res += cnt;
            break;
        }
    }
    return res;
}


let cap = 2;
let n = 2;
let deliveries = [0, 6];
let pickups = [0, 0];

console.log(solution(cap, n, deliveries, pickups));

// solution 2
// 배달과 회수 독립적으로 생각 가능
// 배달에서 최대 cap, 회수에서 최대 cap
// 이를 각 지점에서 알맞게 사용한다고 가정 -> 특정 지점에서의 잉여량은 다음 지점으로