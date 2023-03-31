function solution(storey) {
    let cnt = 0;
    
    while (storey){
        let cur = storey % 10;

        if (cur >= 6){
            storey += 10 - cur;
            cnt += 10 - cur;
        } else if (cur == 5 && parseInt(storey / 10) % 10 >= 5){
            storey += 10 - cur;
            cnt += 10 - cur;
        } else {
            storey -= cur;
            cnt += cur;
        }
        storey = parseInt(storey / 10);
    }
    console.log(cnt);
    return cnt;
}

let storey = 95;  //6
// let storey = 545;   //14
solution(storey);
