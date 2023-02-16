const input = require('fs').readFileSync('/Users/leesonghee/projects/algorithm_study/구/SongheeLee/input.txt').toString().trim().split('\n');


const [N, M] = input.shift().split(' ').map(Number);
const map = input.map((row) => row.split('').map(Number));


class NodeQueue{
    constructor(value){
        this.next = null;
        this.value = value;
    }
}
class Queue{
    constructor (){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
    enqueue(value){
        let nodeQueue = new NodeQueue(value);
        if(this.size == 0){
            this.head = nodeQueue;
        }else{
            this.tail.next = nodeQueue;
        }
        this.tail = nodeQueue;
        this.size++;
    }
    dequeue(){
        if(this.size== 0){
            return null;
        }
        let value = this.head.value;
        this.head = this.head.next;
        this.size--;
        if(this.size == 0){
            this.tail = null;
        }
        return value;
    }
    isEmpty(){
        return this.size == 0;
    }}
    let visited = Array.from({length: N}, () => 0);

    for (let i = 0; i < visited.length; i++) {
        visited[i] = Array.from({length: M}, () => 0);
    }
function bfs(x,y) {
let q = new Queue();
console.log(map);

console.log('N: ', N);
console.log('M: ', M);
visited[x][y] = 1;
    while( x<N || y<M) {
        
        console.log('x: ', x);
console.log('y: ', y);

        if (x+1<N && visited[x+1][y] === 0 && map[x+1][y] === 1) {
            visited[x+1][y] = visited[x][y] + 1;
                q.enqueue({'x':x+1, 'y':y});
        }
        if (y+1<M && visited[x][y+1] === 0 && map[x][y+1] === 1) {
            visited[x][y+1] = visited[x][y] + 1;
            q.enqueue({'x':x, 'y':y+1});
        }
        if (x>0 && visited[x-1][y] === 0 && map[x-1][y] === 1) {
            visited[x-1][y] = visited[x][y] + 1;
                q.enqueue({'x':x-1, 'y':y});
        }
        if (y>0 && visited[x][y-1] === 0 && map[x][y-1] === 1) {
            visited[x][y-1] = visited[x][y] + 1;
            q.enqueue({'x':x, 'y':y-1});
        }
        node = q.dequeue();
        
        x = node.x;
        y = node.y;

        if (x===N-1 && y ===M-1) {
            return (visited[x][y]);
        }
    }
}



console.log(bfs(0,0));


