function solution(sequence) {
    let result = 0;
  
    const tmp_a = [];
    const tmp_b = [];
  
    for (let i = 0; i < sequence.length; i++) {
      if (i === 0) {
        tmp_a.push(sequence[i]);
        tmp_b.push(-sequence[i]);
      } else if (i % 2 === 0) {
        tmp_a.push(Math.max(tmp_a[i - 1] + sequence[i], sequence[i]));
        tmp_b.push(Math.max(tmp_b[i - 1] - sequence[i], -sequence[i]));
      } else {
        tmp_a.push(Math.max(tmp_a[i - 1] - sequence[i], -sequence[i]));
        tmp_b.push(Math.max(tmp_b[i - 1] + sequence[i], sequence[i]));
      }
      result = Math.max(result, tmp_a[i], tmp_b[i]);
    }
    console.log(result);
    return result;
  }
  
  let sequence = [2, 3, -6, 1, 3, -1, 2, 4]; //10
  solution(sequence);
  