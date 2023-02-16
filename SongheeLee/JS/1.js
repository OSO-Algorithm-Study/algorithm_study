function solution(array) {
    array.sort((a,b)=>a-b);
    let count = 0;
    let maxCount = 0;

    let num = -1;
    array.forEach(function(elem){
        if (num === elem) {
            count += 1;
        }
        else {
            if (maxCount<count) {
                maxCount = count;
                }
            else if (maxCount === count)
                return -1;
            
            num = elem;
            count = 1;
            
        }
   
})
    return(maxCount)
}

solution([1, 2, 3, 3, 3, 4]);