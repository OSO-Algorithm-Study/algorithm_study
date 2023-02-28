function solution(board) {
  board = board.map((element) => element.split("")).flat();
  let o_count = 0;
  let x_count = 0;

  for (let i = 0; i < board.length; i++) {
    if (board[i] == "O") {
      o_count++;
    } else if (board[i] == "X") {
      x_count++;
    }
  }

  if (o_count < x_count || o_count - x_count > 1) return 0;

  let o_win = check(board, "O");
  let x_win = check(board, "X");

  if (o_win && x_win) return 0;
  if (o_win && o_count <= x_count) return 0;
  if (x_win && o_count != x_count) return 0;

  return 1;
}

function check(board, sign) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let [a, b, c] of lines) {
    if (board[a] == sign && board[b] == sign && board[c] == sign) return true;
  }
  return false;
}

let board = ["O.X", ".O.", "..X"]; //선공이 "O", 후공이 "X"
solution(board);
