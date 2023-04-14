function solution(n, roads, sources, destination) {
    let answer = [];
    const graph = Array.from({ length: n + 1 }, () => []);
    for (let [a, b] of roads){
        graph[a].push(b);
        graph[b].push(a);
    }
    
    const visited = Array(n+1).fill(Infinity);
    function bfs(a){
        const queue = [a];
        visited[a] = 0;
        
        while (queue.length){
            let idx = queue.shift();
            for (let i of graph[idx]){
                // 다음 방문지의 뎁스가 기존보다 낮으면 갱신.(최소 경로를 보장하기 위해)
                if (visited[idx] + 1 < visited[i]){
                    visited[i] = visited[idx] + 1;
                    queue.push(i);
                }
            }
        }
        
    }
    
    
    bfs(destination);
    answer = sources.map((a) => {
        if (visited[a] == Infinity) return -1;
        else return visited[a];
    })
    
    return answer;
}