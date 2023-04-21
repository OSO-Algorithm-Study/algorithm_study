function solution(n, roads, sources, destination) {
    
    var answer = [];
    let graph = Array.from({ length: n + 1 }, () => []);
    let visited = Array.from({ length: n + 1 }, () => -1);
    
    for (const road of roads) {
        graph[road[0]].push(road[1]);
        graph[road[1]].push(road[0]);
    }
    
    const bfs = (end) => {        
        let queue = [end]
        visited[end] = 0;
        
        while (queue.length) {
            let now = queue.shift();
            
            for (const element of graph[now]) {
                if (visited[element] === -1) {
                    queue.push(element);
                    visited[element] = visited[now] + 1;
                }
            }
        }
    };

    bfs(destination);
    
    for (const source of sources) {
        answer.push(visited[source]);
    }
    
    return answer;
}

const n = 5;
const roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]];
const sources = [1, 3, 5];
const destination = 5;

console.log(solution(n, roads, sources, destination));