function solution(arrayA, arrayB) {
    var answer = 0;
    
    arrayA.sort((a,b) => a-b);
    arrayB.sort((a,b) => a-b);
    
    answer = Math.max(validate(arrayA, arrayB), validate(arrayB, arrayA));
    
    function validate(arr_a, arr_b) {
        for (let i = arr_a[0]; i > 1; i--){
            if (arr_a.every((a) => a %i == 0) && arr_b.every((a) => a % i != 0)) 
                return i;
        }
        return 0;
    }
    return answer;
}