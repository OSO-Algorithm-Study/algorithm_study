function solution(weights) {
    let answer = 0;
    const store = {}; 
    const cal = [1, 3/2, 2, 4/3]; 

    weights.sort((a,b) => b-a);
    for (let i =0; i < weights.length; i++){
        cal.forEach((e) =>{
            let w;
            if (w = weights[i] * e, store[w]){
                answer += store[w];
            }
        });
        if (!store[weights[i]]){
            store[weights[i]] = 1;
        } else {
            store[weights[i]]++;
        }
    }
    console.log(answer);
    return answer;
}

let weights = [100, 180, 360, 100, 270]; // 4
solution(weights);
