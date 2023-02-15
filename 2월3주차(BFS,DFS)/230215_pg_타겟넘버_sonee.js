let count = 0;

function solution(numbers, target) {
    
    let result = 0;
    let curr = 0;
    
    dfs(numbers, result, curr, target, '+');
    dfs(numbers, result, curr, target, '-');
    
    return count;
}

function dfs(graph, result, curr, target, operator) {
    if (operator === '+'){
        result += graph[curr];
    }
    else if (operator === '-') {
        result -= graph[curr];
    }
    
    if (curr === graph.length-1) {
        if (result === target) {
            count += 1;
        }
        return;
    }
    else{
        dfs(graph, result, curr+1, target, '+');
        dfs(graph, result, curr+1, target, '-');
    }
    }
