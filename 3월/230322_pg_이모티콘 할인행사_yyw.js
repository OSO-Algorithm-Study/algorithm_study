function solution(users, emoticons) {
    // 1. 이모티콘 할인율 배열 만들기
    // 2. 이모티콘 구매 전체경우의 수
    // 3. 구한 경우의 수 가입자 수와 판매량으로 변환
    // 4. 가입자 수로 정렬, 가입자 수가 같으면 판매량으로 정렬
    let discount = [0.9, 0.8, 0.7, 0.6];
    let discount_1 = [10, 20, 30, 40]; 
    
    function bfs (){
        const queue = [];
        const result = [];
        queue.push([0, Array(users.length).fill(0)]);
        
        while(queue.length){
            let [depth, price] = queue.pop();
            if (depth >= emoticons.length){
                continue;
            }
            for (let k =0; k < discount.length; k++){
                let tmp = [];
                for (let user of users){
                    if ((user[0]) <= discount_1[k]){
                        tmp.push(emoticons[depth] * discount[k]);
                    } else{
                        tmp.push(0);
                    }
                }
                let new_price = price.map((a,b) => a+tmp[b]);
                queue.push([depth+1, new_price]);
                if (depth == emoticons.length-1){
                    result.push(new_price);
                }
            }
        }
        console.log(result);
        return result;
    }
    
    let arr = bfs();
    let result = [];
    for (let a of arr ){
        let subscriber = 0;
        let sales = 0;
        for (let i =0; i < users.length; i++){
            if (users[i][1] <= a[i]){
                subscriber ++;
            } else{
                sales += a[i];
            }
        }
        result.push([subscriber, sales]);
    }
    result.sort((a,b) => {
        if (a[0] != b[0]) return b[0] - a[0];
        return b[1] -a[1];
    })
    return result[0];
}

let users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]];
let emoticons = [1300, 1500, 1600, 4900]; //[4, 13860]
solution(users, emoticons);