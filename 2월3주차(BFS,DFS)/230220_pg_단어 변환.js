function solution(begin, target, words) {
  const abc = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  const visited = Array(words.length).fill(false);
  const queue = [];
  queue.push([begin, 0]);

  while (queue.length) {
    let [pop_word, count] = queue.shift();

    if (pop_word == target) {
      console.log(count);
      return count;
    }
    for (i = 0; i < begin.length; i++) {
      for (j = 0; j < abc.length; j++) {
        let tmp =
          pop_word.slice(0, i) + abc[j] + pop_word.slice(i + 1, begin.length);
        let idx = words.findIndex((a) => a == tmp);
        if (idx == -1) continue;
        else if (visited[idx] == false) {
          queue.push([tmp, count + 1]);
          visited[idx] = true;
        }
      }
    }
  }
  console.log(0);
  return 0;
}

let begin = "hit";
let target = "cog";
let words = ["hot", "dot", "dog", "lot", "log", "cog"];
solution(begin, target, words);
