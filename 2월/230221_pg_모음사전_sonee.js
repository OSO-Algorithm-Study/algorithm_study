function solution(word) {
    const moem = ['A', 'E', 'I', 'O', 'U'];
    let order = 0;
    for (let i = 0; i < word.length; i++) {
        for (let j = 0; j < moem.length; j++) {
            if (word[i] === moem[j]) {
                order += 1;
                break;
            }
            if (i === 0) order += (5**0 + 5**1 + 5**2 + 5**3 + 5**4);
            if (i === 1) order += (5**0 + 5**1 + 5**2 + 5**3);
            if (i === 2) order += (5**0 + 5**1 + 5**2);
            if (i === 3) order += (5**0 + 5**1);
            if (i === 4) order += (5**0);
            }
        }

    return order;
}