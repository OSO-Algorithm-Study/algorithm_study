function solution(cap, n, deliveries, pickups) {
  let answer = 0;

  let [d, p] = [0, 0];
  for (let i = n-1; i >= 0; i--) {
    d += deliveries[i];
    p += pickups[i];

    let count = 0;
    while (d > 0 || p > 0){
        d -= cap;
        p -= cap;
        count++;
    }
    answer += (i+1) * 2 * count;
  }
  console.log(answer);
  return answer;
}

let cap = 4;
let n = 5;
let deliveries = [1, 0, 3, 1, 2];
let pickups = [0, 3, 0, 4, 0];

// solution(cap, n, deliveries, pickups); // 16
solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]); // 50