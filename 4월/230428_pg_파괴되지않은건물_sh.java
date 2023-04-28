// 시간복잡도 계산 (행 : N / 열 : M / skill : K)
// 최종 시간복잡도 : K + (N * M)

// N <= 1000 / M <= 1000 / K <= 250000
// CASE 1) N * M * K 일때 = 25 * 10^10 (브루트 포스) 250,000,000,000
// CASE 2) K + N * M 일때 = 25 + 10^6  (현재 풀이) 25 + 1,000,000


// 풀이 참고 : https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

class Solution {
    
    // 시간복잡도 : O(1)
    public static void recordStart(int[][] board, int subject, int fromRow, int fromCol, int toRow, int toCol, int damage){
        int initRow = board.length;
        int initCol = board[0].length;
        
        if (subject == 1){
            damage *= -1;
        }
        
        board[fromRow][fromCol] += damage;
        
        if (toRow + 1 < initRow){
            board[toRow + 1][fromCol] += damage * (-1);
        }
        
        if (toCol + 1 < initCol){
            board[fromRow][toCol + 1] += damage * (-1);
        }
        
        if (toCol + 1 < initCol && toRow + 1 < initRow){
            board[toRow + 1][toCol + 1] += damage;
        }
    }
    
    // 시간복잡도 : O(N * M)
    public static void cumulativeSum(int[][] board){
        int row = board.length;
        int col = board[0].length;
        int sum, prevRow, prevCol;
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if (j == 0){
                } else {
                    board[i][j] += board[i][j-1];
                }
            }
        }
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if (i == 0){
                } else {
                    board[i][j] += board[i-1][j];
                }
            }
        }
    }
    
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int subject, fromRow, fromCol, toRow, toCol, damage; 
        int initRow = board.length;
        int initCol = board[0].length;
        
        int[][] initBoard = new int[initRow][initCol];
        
        for(int i = 0; i < skill.length; i++){
            subject = skill[i][0];
            fromRow = skill[i][1];
            fromCol = skill[i][2];
            toRow = skill[i][3];
            toCol = skill[i][4];
            damage = skill[i][5];
            
            // 시간복잡도 : K
            recordStart(initBoard, subject, fromRow, fromCol, toRow, toCol, damage);
        }
        
        cumulativeSum(initBoard);
        
        
        // 시간복잡도 : N * M
        for(int k = 0; k < initBoard.length; k++){
            for(int m = 0; m < initBoard[k].length; m++){
                board[k][m] += initBoard[k][m];         
                
                if(board[k][m] > 0){
                    answer++;
                }
            }
        }
        
        
        return answer;
    }
}