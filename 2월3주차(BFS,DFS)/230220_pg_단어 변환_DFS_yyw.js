function solution(begin, target, words) {
  const visited = Array(words.length).fill(false);
  let count = 0;
  let sub_count = 0;

  const dfs = (begin) => {
    if (begin == target) {
      count = sub_count;
      return;
    }
    for (let i = 0; i < words.length; i++) {
      if (isvalid(begin, words[i]) && !visited[i]) {
        visited[i] = true;
        sub_count += 1;
        dfs(words[i]);
        visited[i] = false;
        sub_count -= 1;
      }
    }
  };

  dfs(begin);
  console.log(count);
  return count;
}

function isvalid(a, b) {
  let count = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i] != b[i]) count++;
  }
  return count == 1 ? true : false;
}

let begin = "hit";
let target = "cog";
let words = ["hot", "dot", "dog", "lot", "log"];
solution(begin, target, words);
