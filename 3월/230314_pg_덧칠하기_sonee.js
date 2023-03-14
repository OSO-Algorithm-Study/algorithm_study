function solution(n, m, section) {
    
    let wall = 0;
    let count = 0;
    while (section.length > 0) {
        wall = section.pop();
        count++;
        if (wall - m >= 0) {    // 길이 >= 0
            while (section.at(-1) > wall - m) { // 마지막 원소가 페인트칠 범위 안에 있다면
                section.pop();
            }      
        }
        else {  // 범위 벗어나면 마지막 페인트칠로 끝
            break;
        }
    }
    
    return count;
}