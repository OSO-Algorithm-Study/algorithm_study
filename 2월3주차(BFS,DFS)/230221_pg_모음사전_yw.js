function solution(word) {
  let answer = 0;
  let alphabet = ["A", "E", "I", "O", "U"];

  for (let i = 0; i < word.length; i++) {
    for (let j = 0; j < alphabet.length; j++) {
      if (word[i] === alphabet[j]) {
        if (i == 0) {
          answer += (5 ** 0 + 5 ** 1 + 5 ** 2 + 5 ** 3 + 5 ** 4) * j + 1;
        } else if (i == 1) {
          answer += (5 ** 0 + 5 ** 1 + 5 ** 2 + 5 ** 3) * j + 1;
        } else if (i == 2) {
          answer += (5 ** 0 + 5 ** 1 + 5 ** 2) * j + 1;
        } else if (i == 3) {
          answer += (5 ** 0 + 5 ** 1) * j + 1;
        } else {
          answer += 5 ** 0 * j + 1;
        }
      }
    }
  }
  return answer;

  //   // DFS
  //   let count = 0;

  //   function dfs(cur) {
  //     if (cur === word) {
  //       answer = count;
  //       return;
  //     }
  //     if (cur.length >= 5) {
  //       return;
  //     }
  //     for (let i = 0; i < alphabet.length; i++) {
  //       let temp = cur + alphabet[i];
  //       count += 1;
  //       dfs(temp);
  //     }
  //   }
  //   dfs("");

  //   return answer;
}
