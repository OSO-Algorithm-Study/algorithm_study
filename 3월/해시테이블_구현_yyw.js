function hashStringToInt(s, tableSize) {
  let hash = 17;

  for (let i = 0; i < s.length; i++) {
    hash = (13 * hash * s.charCodeAt(s[i])) % tableSize;
  }
  return hash;
}

class HashTable {
  constructor() {
    this.table = new Array(3);
    this.numItems = 0;
  }

  setItem = (key, value) => {
    this.numItems++;
    const loadFactor = this.numItems / this.table.length;

    if (loadFactor >= 0.8) {
      this.resize();
    }

    let idx = hashStringToInt(key, this.table.length);

    if (this.table[idx]) {
      this.table[idx].push([key, value]);
    } else {
      this.table[idx] = [[key, value]];
    }
  };

  getItem = (key) => {
    let idx = hashStringToInt(key, this.table.length);

    if (!this.table[idx]) return null;

    return this.table[idx].find((el) => el[0] === key)[1];
  };

  resize = () => {
    const newTable = new Array(this.table.length * 2);

    this.table.forEach((el) => {
      if (el) {
        el.forEach(([key, value]) => {
          const idx = hashStringToInt(key, newTable.length);
          if (newTable[idx]) {
            newTable[idx].push([key, value]);
          } else {
            newTable[idx] = [[key, value]];
          }
        });
      }
    });
    this.table = newTable;
  };
}

const myTable = new HashTable();
myTable.setItem("one", "hello");
myTable.setItem("two", "okay");
myTable.setItem("three", "gogo");
console.log(myTable.getItem("two"));
console.log(myTable.getItem("one"));
console.log(myTable.getItem("three"));
