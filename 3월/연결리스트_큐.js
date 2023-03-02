// 연결리스트의 노드 클래스 정의.
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

// 큐 클래스 정의.
class queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  //큐에 데이터 추가.
  enqueue(data) {
    const node = new Node(data);

    if (this.tail === null) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }

  // 큐에 데이터 제거하고 반환.
  dequeue() {
    if (this.head === null) {
      return null;
    }
    const data = this.head.data;
    this.head = this.head.next;
    if (this.head === null) {
      this.tail = null;
    }
    this.size--;
    return data;
  }

  // 큐의 맨 앞에 있는 데이터를 반환합니다.
  peek() {
    return this.head ? this.head.data : null;
  }

  // 큐가 비어 있는지 확인.
  isEmpty() {
    return this.size === 0;
  }

  // 큐의 크기 반환.
  getSize() {
    return this.size;
  }

  // 큐의 모든 리스트 배열로 반환.
  toArray() {
    const result = [];

    let current = this.head;
    while (current) {
      result.push(current.data);
      current = current.next;
    }
    return result;
  }
}
