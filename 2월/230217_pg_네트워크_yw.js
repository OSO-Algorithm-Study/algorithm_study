function solution(n, computers) {
  let answer = 0;
  let visited = Array.from({ length: n }, () => false);

  // BFS
  function bfs(x) {
    let queue = [x];
    visited[x] = true;

    while (queue.length) {
      let c = queue.shift();
      for (let i = 0; i < n; i++) {
        if (visited[i] == false && computers[c][i] == 1) {
          visited[i] = true;
          queue.push(i);
        }
      }
    }
  }
  for (let j = 0; j < n; j++) {
    if (visited[j] == false) {
      bfs(j);
      answer += 1;
    }
  }

  return answer;
}

// DFS - Recursion
function solution(n, computers) {
  let answer = 0;
  let visited = Array.from({ length: n }, () => false);

  function dfs(x) {
    visited[x] = true;

    for (let i = 0; i < n; i++) {
      if ((visited[i] == false) & (computers[x][i] == 1)) {
        dfs(i);
      }
    }
  }

  for (let j = 0; j < n; j++) {
    if (visited[j] == false) {
      dfs(j);
      answer += 1;
    }
  }

  return answer;
}

// DFS - Stack
function solution(n, computers) {
  let answer = 0;
  let visited = Array.from({ length: n }, () => false);

  function dfs(x) {
    let stack = [x];
    visited[x] = true;

    while (stack.length) {
      k = stack.pop();
      for (let i = 0; i < n; i++) {
        if (visited[i] == false && computers[k][i] == 1) {
          visited[i] = true;
          stack.push(i);
        }
      }
    }
  }

  for (let j = 0; j < n; j++) {
    if (visited[j] == false) {
      dfs(j);
      answer += 1;
    }
  }

  return answer;
}
