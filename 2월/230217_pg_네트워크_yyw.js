function solution(n, computers) {
  var answer = 0;
  let visited = Array.from({ length: n + 1 }, () => 0);

  const bfs = (row) => {
    const queue = [];
    queue.push(row);

    while (queue.length) {
      let x = queue.shift();
      visited[x] = 1;
      for (let i = 0; i < n; i++) {
        if (visited[i] == 0 && computers[x][i] == 1) {
          queue.push(i);
        }
      }
    }
  };

  for (let j = 0; j < n; j++) {
    if (visited[j] == 0) {
      answer++;
      bfs(j);
    }
  }
  console.log(answer);
  return answer;
}

let n = 3;
const computers = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];
solution(n, computers);
