function solution(scores) {
  const wanho = scores[0];
  const wanhoAdd = scores[0][0] + scores[0][1];

  scores.sort((a, b) => {
    if (a[0] != b[0]) return b[0] - a[0];
    return a[1] - b[1];
  });

  let count = 1;
  let max_in1 = 0;
  for (let el of scores) {
    if (wanho[0] < el[0] && wanho[1] < el[1]) return -1;

    if (max_in1 <= el[1]) {
      if (wanhoAdd < el[0] + el[1]) {
        count++;
        max_in1 = el[1];
      }
    }
  }
  console.log(count);
  return count;
}

let scores = [
  [2, 2],
  [1, 4],
  [3, 2],
  [3, 2],
  [2, 1],
]; // 4
solution(scores);
