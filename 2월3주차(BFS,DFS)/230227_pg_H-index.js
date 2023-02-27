function solution(citations) {
  var answer = [];
  citations.sort((a, b) => b - a);

  for (let i = 0; i < citations[0]; i++) {
    let quote_arr = citations.filter((c) => c >= i);
    if (quote_arr.length >= i && citations.length - quote_arr.length <= i) {
      answer.push(i);
    }
  }
  if (answer.length) {
    console.log(answer[answer.length - 1]);
    return answer[answer.length - 1];
  } else return 0;
}

const citations = [3, 0, 6, 1, 5];

solution(citations);
