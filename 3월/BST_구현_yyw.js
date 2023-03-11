class TreeNode {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert = (data) => {
    const node = new TreeNode(data);

    if (this.root === null) {
      this.root = node;
      return this;
    }

    let current = this.root;

    while (current) {
      if (current.data === data) return;

      if (data < current.data) {
        if (!current.left) {
          current.left = node;
          break;
        }
        current = current.left;
      }

      if (data > current.data) {
        if (!current.right) {
          current.right = node;
          break;
        }
        current = current.right;
      }
    }
  };

  getTree = () => {
    const result = [];
    const queue = [];
    queue.push(this.root);

    while (queue.length > 0) {
      let popData = queue.shift();
      result.push(popData.data);
      if (popData.left !== null) queue.push(popData.left);
      if (popData.right !== null) queue.push(popData.right);
    }
    return result;
  };
}

let mybst = new BinarySearchTree();
mybst.insert(10);
mybst.insert(5);
mybst.insert(11);
mybst.insert(7);
mybst.insert(6);
mybst.insert(9);
mybst.insert(3);
console.log(mybst.getTree());
