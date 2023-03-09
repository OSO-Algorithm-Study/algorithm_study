class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class Linked_list {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  //첫번째에 삽입.
  first_insert(data) {
    const node = new Node(data);

    if (this.head === null) {
      this.head = node;
      this.tail = node;
      this.size++;
    } else {
      node.next = this.head;
      this.head = node;
      this.size++;
    }
  }

  //끝에 삽입.
  last_insert(data) {
    const node = new Node(data);

    if (this.tail === null) {
      this.head = node;
      this.tail = node;
      this.size++;
    } else {
      this.tail.next = node;
      this.tail = node;
      this.size++;
    }
  }

  //중간에 삽입.
  insert(data, index) {
    const node = new Node(data);

    let comp_idx = 0;
    if (index > 0 && index > this.size) {
      return;
    }
    if (this.head === null) {
      this.head = node;
      this.tail = node;
      this.size++;
    } else {
      let current = this.head;
      let previous;
      let count = 0;
      while (count < index) {
        count++;
        previous = current;
        current = current.next;
      }
      previous.next = node;
      node.next = current;
      this.size++;
      if (index == this.size - 1) this.tail = node;
    }
  }

  //노드 삭제.
  delete(index) {
    if (index > 0 && index > this.size) return null;

    let current = this.head;
    let previous;
    let count = 0;
    if (index === 0) {
      this.head = current.next;
    } else {
      while (count < index) {
        count++;
        previous = current;
        current = current.next;
      }
      previous.next = current.next;
    }

    this.size--;
  }

  //연결 리스트 값들 전체 확인.
  printListData() {
    const arr = [];
    let current = this.head;

    while (current !== null) {
      arr.push(current.data);
      current = current.next;
    }
    return arr;
  }
}

const link_list = new Linked_list();
link_list.first_insert(5);
link_list.insert(3, 1);
link_list.last_insert(7);
link_list.insert(8, 3);
link_list.insert(9, 1);
link_list.delete(1);
console.log(link_list.printListData(), link_list.size);
