// const input = require('fs').readFileSync('/Users/leesonghee/projects/algorithm_study/구/SongheeLee/input.txt').toString().trim().split('\n');
// // const input = require('fs')
// // .readFileSync('/dev/stdin')
// // .toString()
// // .trim()
// // .split('\n');

const fs = require("fs");
let filePath = process.platform === "linux" ? "/dev/stdin" : "/Users/leesonghee/projects/algorithm_study/구/SongheeLee/input.txt";
let input = fs.readFileSync(filePath).toString().trim();
input = input.split("\n");

const city = +input[0];
const bus = +input[1];

if(city === 1){
  console.log(0);
  return;
}
if(bus === 1){
  const [x, y, cost] = input[2].split(" ").map((e) => +e);
  console.log(cost);
  return;
}
let paths = [];
for (let i = 2; i < bus + 2; i++) {
  paths.push(input[i].split(" ").map((e) => +e));
}

const [startPoint, endPoint] = input[bus + 2].split(" ").map((e) => +e);

let adj = Array.from(Array(city + 1), () => Array());

paths.forEach(([start, end, cost]) => {
  adj[start].push([end, cost]);
});

console.log("paths", paths);
console.log("adj", adj);

console.log(d(startPoint, endPoint));



function d(startPoint, endPoint) {

    class PriorityQueue {
        constructor() {
          this.values = [];
        }
        enqueue(val, priority) {
          this.values.push({ val, priority });
          this.sort();
        }
        dequeue() {
          return this.values.shift();
        }
        sort() {
          this.values.sort((a, b) => a.priority - b.priority);
        }
      }

    let heapque = new PriorityQueue();
    adj[startPoint].forEach(([end, cost]) => {
        heapque.enqueue(end, cost);
      });
    while(heapque.values.length> 0) {
      let node =  heapque.dequeue();
      let sum = node.priority;
      let end = node.val;
    if (end === endPoint) {
        return sum;
    }
      adj[end].forEach(([end, cost]) => {
        heapque.enqueue(end, sum+cost);
      });
    }
    }
    