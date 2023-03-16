function solution(sequence) {
    
	let MaxSum = 0;
	let ThisSum = 0;
	
    for (let i = 0; i < sequence.length; i++) {
        
        if (i%2 === 0) {
            num = -sequence[i];
        }
        else {
            num = sequence[i];
        }
        
        ThisSum + num > 0 ? ThisSum = ThisSum + num : ThisSum = 0;
        
        if (MaxSum < ThisSum) {
            MaxSum = ThisSum
        }
	}
    
    let MaxSum2 = 0;
	ThisSum = 0;
    
    for (let i = 0; i < sequence.length; i++) {
        
        if (i%2 === 1) {
            num = -sequence[i];
        }
        else {
            num = sequence[i];
        }
        
        ThisSum + num > 0 ? ThisSum = ThisSum + num : ThisSum = 0;
        
        if (MaxSum2 < ThisSum) {
            MaxSum2 = ThisSum
        }
	}
	
    if (MaxSum > MaxSum2) {
        return MaxSum
    }
    else {
        return MaxSum2
    }
    
}