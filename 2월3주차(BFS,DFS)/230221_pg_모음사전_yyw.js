function solution(word) {
  var answer = 0;
  let count = 0;
  const words_dic = ["A", "E", "I", "O", "U"];

  const dfs = (curr) => {
    if (curr.length >= 5 || curr == word) {
      if (curr == word) {
        answer = count;
        return;
      }
      return;
    }
    for (let i = 0; i < words_dic.length; i++) {
      let curr_word = curr + words_dic[i];
      count++;
      dfs(curr_word);
    }
  };

  dfs("");
  console.log(answer);
  return answer;
}

let word = "EIO";
solution(word);
