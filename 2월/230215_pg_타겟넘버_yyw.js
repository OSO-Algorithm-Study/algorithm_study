// 노드 클래스를 정의합니다.
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  // 큐 클래스를 정의합니다.
  class Queue {
    constructor() {
      this.front = null;
      this.rear = null;
      this.size = 0;
    }
  
    // 큐에 데이터를 추가합니다.
    enqueue(data) {
      const node = new Node(data);
      if (this.rear === null) {
        this.front = node;
        this.rear = node;
      } else {
        this.rear.next = node;
        this.rear = node;
      }
      this.size++;
    }
  
    // 큐에서 데이터를 제거하고 반환합니다.
    dequeue() {
      if (this.front === null) {
        return null;
      }
      const data = this.front.data;
      this.front = this.front.next;
      if (this.front === null) {
        this.rear = null;
      }
      this.size--;
      return data;
    }
  
    // 큐의 맨 앞에 있는 데이터를 반환합니다.
    peek() {
      return this.front ? this.front.data : null;
    }
  
    // 큐가 비어 있는지 확인합니다.
    isEmpty() {
      return this.size === 0;
    }
  
    // 큐의 크기를 반환합니다.
    getSize() {
      return this.size;
    }
  }
  
  function solution(numbers, target) {
    var answer = 0;
  
    const queue = new Queue();
    const length = numbers.length;
  
    queue.enqueue([numbers[0], 0]);
    queue.enqueue([-numbers[0], 0]);
  
    while (!queue.isEmpty()) {
      const [num, count] = queue.dequeue();
      if (count + 1 == length) {
        if (num == target) answer += 1;
      } else {
        queue.enqueue([num + numbers[count + 1], count + 1]);
        queue.enqueue([num - numbers[count + 1], count + 1]);
      }
    }
    console.log(answer);
    return answer;
  }
  
  let numbers = [1, 1, 1, 1, 1];
  let target = 3;
  // result = 5;
  
  solution(numbers, target);