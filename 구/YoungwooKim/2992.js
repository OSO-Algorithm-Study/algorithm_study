const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const solution = () => {
    let number = '';
    let minNumber = '999999';
    let digit = input.length;
    let visited = Array.from({ length: digit }, () => false);

    const backtracking = (depth) => {
        if (depth == digit) {
            if (input < number && number < minNumber) minNumber = number;
            return;
        }
        for (let i = 0; i < digit; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            number += input[i];
            backtracking(depth + 1);
            visited[i] = false;
            number = number.slice(0, -1);
        }
    };
    backtracking(0);
    if (minNumber === '999999') minNumber = '0';
    console.log(minNumber);
};

solution();