function solution(maps) {
  let answer = 0;
  let M = maps.length;
  let N = maps[0].length;
  let visited = Array.from({ length: M }, () =>
    Array.from({ length: N }, () => -1)
  );
  let dx = [0, 1, 0, -1];
  let dy = [1, 0, -1, 0];

  function bfs(a, b) {
    let queue = [[a, b]];
    visited[a][b] = 1;
    while (queue.length) {
      let [x, y] = queue.shift();
      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (0 <= nx && nx < M && 0 <= ny && ny < N) {
          if (visited[nx][ny] == -1 && maps[nx][ny] == 1) {
            visited[nx][ny] = visited[x][y] + 1;
            queue.push([nx, ny]);
          }
        }
      }
    }
    return visited[M - 1][N - 1];
  }
  answer = bfs(0, 0);

  return answer;
}
