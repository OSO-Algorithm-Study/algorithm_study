function solution(n, computers) {

    let network = 0;
    
    for (let i = 0; i < n; i++) {
        if (computers[i][i] === 1) {
            network += 1;
            dfs (i);
        }   
    }
    
    function dfs(start) {
        
        computers[start][start] = 0;
        for (let i = 0; i < n; i++) {
            if (computers[start][i] === 1) {
                computers[start][i] = 0;
                dfs(i);
            }
        }  
    }
    return network;
}