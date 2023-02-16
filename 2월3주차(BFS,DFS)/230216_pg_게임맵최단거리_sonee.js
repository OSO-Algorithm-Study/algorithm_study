function solution(maps) {
    dx = [0, 1, 0, -1] // 오 아 왼 위
    dy = [1, 0, -1, 0]
    
    const width = maps[0].length;
    const height = maps.length;
    
    let visited = Array.from(Array(height), () => Array(width).fill(-1));
    
    function bfs(x,y) { 
    let q = [];
    q.push([x, y]);
    visited[x][y] = 1;
        while(q.length>0)
    {
        let [x, y] = q.shift();

        for (let i = 0 ; i < 4 ; i++) {
           nx = x+dx[i];
            ny = y + dy[i];
        if (0 <= nx && nx<height 
            && 0 <= ny && ny < width
            && visited[nx][ny] < 0
            && maps[nx][ny] === 1 )
        {
            
            visited[nx][ny] =  visited[x][y] + 1;
            q.push([nx, ny]);
        }
            
            if (nx === height -1 && ny === width-1)
           { return (visited[height-1][width-1]);}
    }
    } return -1;}
    
 
    return bfs(0,0);
}