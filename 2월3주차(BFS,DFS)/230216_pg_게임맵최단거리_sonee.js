function solution(maps) {

    const width = maps[0].length;
    const height = maps.length;
    
    // 2차원 배열 선언 및 초기화
    let visited =  Array.from({length: width}, () => -1);
    for (let i = 0; i < visited.length; i++) {
        visited[i] = Array.from({length: height}, () => -1);
    }

    function bfs(x,y) {
        let q = new Queue();
        q.enqueue({'x':0, 'y':0});
        visited[x][y] = 1;

        while(q.size>0) {


            node = q.dequeue();

       
        x = node.x;
        y = node.y;

        if (x+1<height && visited[x+1][y] < 0 && maps[x+1][y] === 1) {
            visited[x+1][y] = visited[x][y] + 1;
                q.enqueue({'x':x+1, 'y':y});
            
        }
        if (y+1<width && visited[x][y+1] < 0 && maps[x][y+1] === 1) {
            visited[x][y+1] = visited[x][y] + 1;
            q.enqueue({'x':x, 'y':y+1});
          
        }
        if (x>0 && visited[x-1][y] < 0 && maps[x-1][y] === 1) {
            visited[x-1][y] = visited[x][y] + 1;
                q.enqueue({'x':x-1, 'y':y});
            
        }
        if (y>0 && visited[x][y-1] < 0 && maps[x][y-1] === 1) {
            visited[x][y-1] = visited[x][y] + 1;
            q.enqueue({'x':x, 'y':y-1});
            
        }
        
       

      
        
    }
        
       
            return (visited[height-1][width-1]);
        
}
    
    return bfs(0,0);
}



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
