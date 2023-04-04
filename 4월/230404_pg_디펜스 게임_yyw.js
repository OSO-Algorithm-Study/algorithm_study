function solution(n, k, enemy) {
    let left = 0;
    let right = enemy.length;
    let mid = 0;

    while(left <= right){
        mid = Math.floor((left + right) / 2);
        let round = enemy.slice(0, mid).sort((a, b) => b-a);        // [4, 2, 4, 5, 3, 3, 1]
        let cheet = k;                                              // [5, 4, 4, 3, 3, 2, 1]
        let soldier = n;
        let curround = mid;

        for (let i = 0; i < round.length; i++) {
            if (cheet > 0) {
                cheet--;
            } else {
                soldier -= round[i];
                if (soldier < 0) {
                    curround = i;
                    break;
                }
            }
        }
        if (mid > curround){
            right = mid - 1;
        } else{
            left = mid + 1;
        }
    
    }
    return right;
}