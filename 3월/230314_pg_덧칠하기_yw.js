function solution(n, m, section) {
    var answer = 0;
    while (section.length) {
        let sec = section.pop();
        while (section[section.length - 1] > sec - m) {
            section.pop();
        }
        answer += 1;
    }
    return answer;
}

// section.at(-1)으로 마지막 원소에 대한 접근이 가능하지만 느림
// 범위 확인 및 음의 인덱스 처리를 위한 추가 오버헤드를 포함