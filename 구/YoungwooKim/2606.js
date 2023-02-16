const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const solution = (graph) => {
  let queue = [1];
  let count = 0;
  while (queue.length) {
    let v = queue.shift();
    if (visited[v]) continue;
    visited[v] = true;
    count++;
    graph[v].forEach((e) => {
      if (!queue.includes(e)) queue.push(e);
    });
  }
  console.log(count - 1);
};

const N = parseInt(input.shift());
const M = parseInt(input.shift());
const visited = Array.from({ length: N + 1 }, () => false);
const graph = Array.from({ length: N + 1 }, () => []);
// const visited = Array(N + 1).fill(false);
// const graph = Array(N + 1).fill([]);

for (let i = 0; i < M; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

solution(graph);
