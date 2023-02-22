function solution(begin, target, words) {

    let minStep = 100;  
    let count = 0;
    let visited = Array.from({length: words.length}, () => 0);

    dfs(begin, 0);

    function dfs (word, step) {

    if (word === target) {
        if (minStep > step) {
            minStep = step;
            // console.log("minStep", minStep);
            return;
        }
    }

    for (let i = 0; i < words.length ; i++) {
        count = 0;
        if(visited[i] === 0) {
        for (let j = 0; j < words[i].length; j++) {
            if (words[i][j] !== word[j]) {
                count++;
            }
        }

        if (count === 1) {
            // console.log("word", word, "words", words[i], "step", step);
            visited[i] = 1;
            dfs(words[i], step+1);
            visited[i] = 0; // dfs 종료 후, visited 초기화
        }
        }
    }
    return;
    }

if (minStep === 100)
    minStep = 0;
    
return minStep;
}