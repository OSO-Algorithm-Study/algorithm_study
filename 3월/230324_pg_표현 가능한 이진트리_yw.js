function solution(numbers) {
    var answer = [];
    
    const isBinaryTree = (tree, start, end) => {
        if (start == end) return true;
        
        let mid = Math.floor((start + end) / 2);
        let leftChild = Math.floor((start + mid - 1) / 2);
        let rightChild = Math.floor((mid + 1 + end) / 2);
        
        if (tree[mid] === '0' && (tree[leftChild] === '1' || tree[rightChild] === '1')) {
            return false;
            
        }
        return isBinaryTree(tree, start, mid - 1) && isBinaryTree(tree, mid + 1, end);
    };
    
    for (let i = 0; i < numbers.length; i++) {
        let binaryNum = numbers[i].toString(2);
        let binaryNumLength = binaryNum.length;
        
        let n = binaryNumLength.toString(2).length;
        let dummy = (2**n - 1) - binaryNumLength;
        let fullBinary = '0'.repeat(dummy) + binaryNum;
        
        if (isBinaryTree(fullBinary, 0, fullBinary.length - 1)) {
            answer.push(1);
        }
        else {
            answer.push(0);
        }
    }
    return answer;
}

const numbers = [7, 42, 5];
console.log(solution(numbers));