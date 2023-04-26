function solution(n, paths, gates, summits) {
    var answer = [1e9, 1e9];
    let graph = Array.from({ length: n + 1 }, () => []);
    let intensity = Array.from({ length: n + 1 }, () => 1e9);

    paths.forEach((path) => {
        const [i, j, w] = path;
        graph[i].push([w, j]);
        graph[j].push([w, i]);
    });
    // 단방향으로 변환 (대칭성 활용)
    summits.sort((a, b) => (a - b)).forEach((summit) => {
        graph[summit] = [];
    });

    let queue = [];
    // 출발지에 관계없이 최소 intensity
    gates.forEach((gate) => {
        intensity[gate] = 0;
        queue.push(gate);
    });

    while (queue.length) {
        let from = queue.shift();
        // 다익스트라 변형
        for (const [weight, to] of graph[from]) {
            if (intensity[to] > Math.max(intensity[from], weight)) {
                intensity[to] = Math.max(intensity[from], weight);
                queue.push(to);
            }
        }
    }

    summits.forEach((summit) => {
        if (answer[1] > intensity[summit]) {
            answer[0] = summit;
            answer[1] = intensity[summit];
        }
    });

    return answer;
}

const n = 6;
const paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]];
const gates = [1, 3];
const summits = [5];

console.log(solution(n, paths, gates, summits));