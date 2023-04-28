class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int r_len = board.length;
        int c_len = board[0].length;
        int[][] skArr = new int[r_len + 1][c_len + 1];
        
        int type, r1, c1, r2, c2, degree;
        for (int[] i : skill){
            type = i[0];
            r1 = i[1];
            c1 = i[2];
            r2 = i[3];
            c2 = i[4];
            degree = i[5];
            
            if (type == 1){
                skArr[r1][c1] -= degree;
                skArr[r1][c2 + 1] += degree;
                skArr[r2 + 1][c1] += degree;
                skArr[r2 + 1][c2 + 1] -= degree;
            } else{
                skArr[r1][c1] += degree;
                skArr[r1][c2 + 1] -= degree;
                skArr[r2 + 1][c1] -= degree;
                skArr[r2 + 1][c2 + 1] += degree;
            }
        }
        opArr(skArr);
        
        for (int i = 0; i < r_len; i++){
            for (int j = 0; j < c_len; j++){
                if (board[i][j] + skArr[i][j] > 0){
                    answer++;
                }
            }
        }
        return answer;
    }
    
    public void opArr(int[][] skArr){
        int r_len = skArr.length;
        int c_len = skArr[0].length;
        
        // 상하
        for (int i = 1; i < r_len; i++){
            for (int j = 0; j < c_len; j++){
                skArr[i][j] += skArr[i - 1][j];
            }
        }
        // 좌우
        for (int i = 1; i < c_len; i++){
            for (int j = 0; j < r_len; j++){
                skArr[j][i] += skArr[j][i - 1];
            }
        }
    }
}