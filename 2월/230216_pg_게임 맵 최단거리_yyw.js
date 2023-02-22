function solution(maps) {
  var answer = 0;
  const row_len = maps.length;
  const column_len = maps[0].length;
  let visited = Array.from({ length: row_len }, () =>
    Array(column_len).fill(0)
  );

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  function bfs(x, y) {
    let cnt = 0;
    const queue = [];
    queue.push([x, y, 1]);

    while (queue.length) {
      let [x, y, add] = queue.shift();
      if (x == row_len - 1 && y == column_len - 1) {
        return maps[x][y];
      }

      for (i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (0 <= nx && nx < row_len && 0 <= ny && ny < column_len) {
          if (maps[nx][ny] == 1 && visited[nx][ny] == 0) {
            visited[nx][ny] = 1;
            maps[nx][ny] += add;
            queue.push([nx, ny, maps[nx][ny]]);
          }
        }
      }
    }
    return -1;
  }

  answer += bfs(0, 0);
  console.log(answer);
  return answer;
}

maps = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 0, 0, 1],
];

solution(maps);
