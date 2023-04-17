function solution(skill, skill_trees) {
    //1. skill_trees에서 skill이 있는거만 필터링
    //2. 필터링한 배열을 순회하며 유효성 검사.
    let cnt = 0;

    const filterArr = skill_trees.map((a) => {
        return a.split('').filter((b) => skill.includes(b));
    })
    
    for (let arr of filterArr){
        let valid = true;
        for (let i =0; i < arr.length; i++){
            if (arr[i] != skill[i]){
                valid = false;
                break;
            }
        }
        if (valid === true){
            cnt++;
        }
    }
    return cnt;
}