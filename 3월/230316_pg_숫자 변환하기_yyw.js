function solution(x, y, n) {
  const dp = Array(y + 1).fill(Infinity);
  dp[x] = 0;
  for (let i = x; i <= y; i++) {
    if (dp[i] == Infinity) continue;

    if (i + n <= y) {
      dp[i + n] = Math.min(dp[i + n], dp[i] + 1);
    }
    if (i * 2 <= y) {
      dp[i * 2] = Math.min(dp[i * 2], dp[i] + 1);
    }
    if (i * 3 <= y) {
      dp[i * 3] = Math.min(dp[i * 3], dp[i] + 1);
    }
  }

  if (dp[y] === Infinity) {
    console.log(-1);
    return -1;
  }
  console.log(dp[y]);
  return dp[y];
}

let [x, y, n] = [10, 40, 5]; //2
// let [x, y, n] = [10, 40, 30]; //1
// let [x, y, n] = [2, 5, 4]; // -1

solution(x, y, n);
