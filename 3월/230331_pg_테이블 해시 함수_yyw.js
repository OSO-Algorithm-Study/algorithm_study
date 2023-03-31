function solution(data, col, row_begin, row_end) {
    var answer = 0;
    data.sort((a, b) =>{
        if (a[col-1] == b[col-1]) return b[0] - a[0];
        return a[col-1] - b[col-1];
    })
    let rowAddArr = [];
    let tmp = 0;
    for (let i=row_begin-1; i <row_end; i++){
        for (let j =0; j < data[i].length; j++){
            tmp += data[i][j] % (i+1);
        }
        rowAddArr.push(tmp);
        tmp = 0;
    }
    
    answer = rowAddArr[0] ^ rowAddArr[1];
    for (let k=2; k < rowAddArr.length; k++){
        answer ^= rowAddArr[k];
    }
    return answer;
}