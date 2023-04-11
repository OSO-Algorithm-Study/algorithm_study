function solution(k, tangerine) {
    var answer = tangerine.length;
    const map = {};
    
    for (let i=0; i < tangerine.length; i++){
        if (!map[tangerine[i]]){
            map[tangerine[i]] = 1;
        } else{
            map[tangerine[i]] += 1;
        }
    }
    
    const sortedArray = Object.entries(map).sort((a, b) => b[1] - a[1]);
    const sortedMap = new Map(sortedArray);
    
    let cnt = 0;
    for (let [key, value] of sortedMap){
        cnt++;
        k -= value;
        if (k <= 0) break;
    }
    return cnt;
}