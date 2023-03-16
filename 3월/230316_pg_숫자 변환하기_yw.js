function solution(x, y, n) {
    
    class Node {
        constructor(data) {
          this.data = data;
          this.next = null;
        }
      }
    
    class Queue {
        constructor() {
            this.head = null;
            this.tail = null;
            this.size = 0;
        }
    
        enqueue(data) {
            const node = new Node(data);
    
            if (this.tail === null) {
                this.head = node;
                this.tail = node;
            }
    
            else {
                this.tail.next = node;
                this.tail = node;
            }
    
            this.size++;
        }
    
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
    }
    
    const queue = new Queue();
    queue.enqueue(x);
    
    const visited = new Map();
    visited.set(x, 0);
    
    while (queue.size) {
        
        let num = queue.dequeue();
        
        if (num === y) {
            return visited.get(num);
        }
        
        if (!visited.has(num + n) && num + n <= y) {
            visited.set(num + n, visited.get(num) + 1);
            queue.enqueue(num + n);
        }
        
        if (!visited.has(num * 2) && num * 2 <= y) {
            visited.set(num * 2, visited.get(num) + 1);
            queue.enqueue(num * 2);
        }
        
        if (!visited.has(num * 3) && num * 3 <= y) {
            visited.set(num * 3, visited.get(num) + 1);
            queue.enqueue(num * 3);
        }
    }
    
    return -1;
}