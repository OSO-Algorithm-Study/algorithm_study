function solution(users, emoticons) {
    var answer = [];
    let array = [];
    let discRates = [0.1, 0.2, 0.3, 0.4];
    
    function subscribeOrBuy(arr) {
        let res = [0, 0];
        
        for (const user of users) {
            let tot = 0;
            
            for (let i = 0; i < emoticons.length; i++) {
                if (user[0] <= (100 * arr[i])) {
                    tot += emoticons[i] * (1 - arr[i])
                }
            }
            
            if (tot >= user[1]) {
                res[0] += 1;
            }
            else {
                res[1] += tot;
            }
        }
        
        answer.push(res);
    }
    
    function dfs(depth) {
        if (depth == emoticons.length) {
            subscribeOrBuy(array);
            return;
        }
        for (const discRate of discRates) {
            array[depth] = discRate;
            dfs(depth + 1);
        }
    }
    
    dfs(0);
    
    answer.sort((a, b) => {
        if (a[0] == b[0]) {
            return b[1] - a[1];
        }
        return b[0] - a[0];
    });
    
    return answer[0];
}

const users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]];
const emoticons = [1300, 1500, 1600, 4900];
console.log(solution(users, emoticons));