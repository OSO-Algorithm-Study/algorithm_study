// const input = require('fs').readFileSync('/Users/leesonghee/projects/algorithm_study/구/SongheeLee/input.txt').toString().trim().split('\n');
const input = require('fs')
.readFileSync('/dev/stdin')
.toString()
.trim()
.split('\n');


const N = input.shift();
const map = input.map((row) => row.split('').map(Number));

const width = map[0].length;
const height = map.length;

console.log(bfs(0,0));

function bfs(x, y) {

    dx = [1, 0, -1, 0];
    dy = [0, 1, 0, -1];
    
    const  visited = Array.from(new Array(height), () => new Array(width).fill(-1));
    let q = [[y, x]];
    visited[y][x] = 0;
    while(q.length > 0) {
        const [y, x] = q.shift();
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            
            if (nx >= 0 && nx < width && ny >= 0 && ny < height) {
                if (map[ny][nx] === 1 && visited[ny][nx]<0) {
                    visited[ny][nx] = visited[y][x];
                    q.push([ny, nx]);
                }
                else if (map[ny][nx] === 1 && visited[ny][nx] > visited[y][x]) {
                    visited[ny][nx] = visited[y][x];
                    q.push([ny, nx]);
                    
                }
                else if (map[ny][nx] === 0 && visited[ny][nx] > visited[y][x]+1) {
                    visited[ny][nx] = visited[y][x]+1;
                    q.push([ny, nx]);
                    
                }
                else if (map[ny][nx] === 0 && visited[ny][nx]< 0) {
                    visited[ny][nx] = visited[y][x] + 1;
                    q.push([ny, nx]);
                }
            }
        }

    }

return (visited[height-1][width-1]);
}