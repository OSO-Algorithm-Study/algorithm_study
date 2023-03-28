function solution(n, m, x, y, r, c, k) {
  var answer = " ";
  let start = [x, y];
  let end = [r, c];
  const graph = Array.from({ length: n + 1 }, () => Array(m + 1).fill(false));
  graph[r][c] = 0;

  const dx = [1, 0, 0, -1];
  const dy = [0, -1, 1, 0];
  const xys = ["d", "l", "r", "u"];
  let flg = 0;

  function dfs(x1, y1, cnt, str) {
    if (cnt == k && graph[x1][y1] === 0) {
      answer = str;
      flg = 1;
      return;
    }

    if (Math.abs(r - x1) + Math.abs(c - y1) + cnt > k) {
      return;
    }

    if (graph[x1][y1] === 0 && (k - cnt / 2) % 2 === 0) {
      answer += (k - (cnt + 1) / 2) * "rl";
    }

    for (let i = 0; i < 4; i++) {
      let nx = x1 + dx[i];
      let ny = y1 + dy[i];

      if (0 < nx && nx <= n && 0 < ny && ny <= m) {
        dfs(nx, ny, cnt + 1, str + xys[i]);
        if (flg == 1) return;
      }
    }
  }

  let InitialValidity = k - Math.abs(r - x) - Math.abs(c - y);
  if (InitialValidity < 0 || InitialValidity % 2 != 0) return "impossible";

  dfs(x, y, 0, "");
  if (flg == 0) return "impossible";
  console.log(answer);
  return answer;
}

let [n, m, x, y, r, c, k] = [3, 3, 1, 2, 3, 3, 4]; //"impossible"
solution(n, m, x, y, r, c, k);
