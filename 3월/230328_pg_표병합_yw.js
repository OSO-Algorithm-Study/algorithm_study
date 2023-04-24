function solution(commands) {
    let root = Array.from({ length: 51 }, (() => Array.from({ length: 51 }, () => [])));
    
    for (let i = 1; i < root.length; i++) {
        for (let j = 1; j < root.length; j++) {
            root[i][j] = [i, j];
        }
    }
    
    function find(a, b) {
        if (root[a][b].join("") === [a, b].join("")) return [a, b];
        return find(root[a][b][0], root[a][b][1]);
    }
    
    function union(a1, b1, a2, b2) {
        let [x, y] = find(a1, b1);
        let [p, q] = find(a2, b2);
        root[p][q] = [x, y];
        return [x, y, p, q];
    }
    
    var answer = [];
    let table = Array.from({ length: 51 }, (() => Array.from({ length: 51 }, () => "EMPTY")));
    
    for (const command of commands) {
        const instruction = command.split(" ");
        if (instruction[0] === "UPDATE") {
            if (instruction.length === 4) {
                let [r, c] = [instruction[1], instruction[2]];
                let [root_r, root_c] = find(r, c);
                let value = instruction[3];
                table[root_r][root_c] = value;
            }
            else {
                let value1 = instruction[1];
                let value2 = instruction[2];
                for (let i = 1; i < table.length; i++) {
                    for (let j = 1; j < table.length; j++) {
                        let [root_i, root_j] = find(i, j);
                        if (table[root_i][root_j] === value1) {
                            table[root_i][root_j] = value2;
                        }
                    }
                }
            }
        }
        
        else if (instruction[0] === "MERGE") {
            let [r1, c1] = [instruction[1], instruction[2]];
            let [r2, c2] = [instruction[3], instruction[4]];
            let [root_r1, root_c1, root_r2, root_c2] = union(r1, c1, r2, c2);
            
            if ((r1 === r2 && c1 === c2) || (root_r1 === root_r2 && root_c1 === root_c2)) continue;

            if (table[root_r1][root_c1] === "EMPTY" && table[root_r2][root_c2] !== "EMPTY") {
                table[root_r1][root_c1] = table[root_r2][root_c2];
            }
        }

        else if (instruction[0] === "UNMERGE") {
            let [r, c] = [instruction[1], instruction[2]];
            let [root_r, root_c] = find(r, c);
            let removeList = [];
            let temp = "EMPTY";
            
            if (table[root_r][root_c] !== "EMPTY") {
                temp = table[root_r][root_c];
            }
            
            for (let i = 1; i < root.length; i++) {
                    for (let j = 1; j < root.length; j++) {
                        if (find(i, j).join("") === [root_r, root_c].join("")) {
                            removeList.push([i, j]);
                        }
                    }
                }

            for (const [x, y] of removeList) {
                root[x][y] = [x, y];
                table[x][y] = "EMPTY";
            }
            table[r][c] = temp;
        }

        else if (instruction[0] === "PRINT") {
            let [r, c] = [instruction[1], instruction[2]];
            let [root_r, root_c] = find(r, c);
            answer.push(table[root_r][root_c]);
        }
    }
    return answer;
}
// const commands = ["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"];
// const commands = ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"];
const commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"];
console.log(solution(commands));