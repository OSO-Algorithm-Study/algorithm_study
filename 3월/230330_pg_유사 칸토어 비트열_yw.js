function solution(n, l, r) {
    var answer = 0;
    
    let quinaryL = (l - 1).toString(5);
    let quinaryR = r.toString(5);
    
    let quinaryLcnt = 0;
    let quinaryRcnt = 0;
    
    for (let i = 0; i < quinaryL.length; i++) {
        let exponent = quinaryL.length - (i + 1);
        let digitNum = parseInt(quinaryL[i]);
        if (digitNum > 2) {
            quinaryLcnt += (digitNum - 1) * (4 ** exponent);
        }
        else if (digitNum == 2) {
            quinaryLcnt += digitNum * (4 ** exponent);
            break;
        }
        else {
            quinaryLcnt += digitNum * (4 ** exponent);
        }
    }
    
    for (let i = 0; i < quinaryR.length; i++) {
        let exponent = quinaryR.length - (i + 1);
        let digitNum = parseInt(quinaryR[i]);
        if (digitNum > 2) {
            quinaryRcnt += (digitNum - 1) * (4 ** exponent);
        }
        else if (digitNum == 2) {
            quinaryRcnt += digitNum * (4 ** exponent);
            break;
        }
        else {
            quinaryRcnt += digitNum * (4 ** exponent);
        }
    }
    
    answer = quinaryRcnt - quinaryLcnt;
    
    return answer;
}