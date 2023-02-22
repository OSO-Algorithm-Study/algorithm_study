function solution(begin, target, words) {
  let answer = 0;
  let visited = Array.from({ length: words.length }, () => false);

  function checkDiff(word1, word2) {
    let cnt = 0;
    for (let i = 0; i < word1.length; i++) {
      if (word1[i] != word2[i]) {
        cnt += 1;
      }
    }
    if (cnt == 1) {
      return true;
    }
    return false;
  }

  function bfs() {
    let count = 0;
    let queue = [[begin, 0]];
    while (queue.length) {
      let [word, count] = queue.shift();
      if (word == target) {
        return count;
      }
      for (let i = 0; i < words.length; i++) {
        if (visited[i] == false && checkDiff(word, words[i])) {
          visited[i] = true;
          queue.push([words[i], count + 1]);
        }
      }
    }
    return 0;
  }
  answer = bfs();

  return answer;

  //   // DFS
  //   let INF = 1e9;
  //   let min = INF;

  //   function dfs(word, count) {
  //     if (word == target) {
  //       min = Math.min(min, count);
  //       return;
  //     }
  //     for (let i = 0; i < words.length; i++) {
  //       if (visited[i] == false && checkDiff(word, words[i])) {
  //         visited[i] = true;
  //         dfs(words[i], count + 1);
  //         visited[i] = false;
  //       }
  //     }
  //   }

  //   dfs(begin, 0);

  //   if (min == INF) {
  //     min = 0;
  //   }

  //   return min;
}
