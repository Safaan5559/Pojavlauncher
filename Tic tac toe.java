import java.util.Scanner;

 class TicTacToe {
    static String[] board = {" ", " ", " ", " ", " ", " ", " ", " ", " "};
    static String currentPlayer = "X";

    static int[][] winningConditions = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // Rows
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // Columns
        {0, 4, 8}, {2, 4, 6}             // Diagonals
    };

    // Print the board with index helper
    public static void printBoard() {
        System.out.println(" " + board[1] + " | " + board[2] + " | " + board[3] + "        1 | 2 | 3");       
        System.out.println("---+---+---      ---+---+---");
        System.out.println(" " + board[4] + " | " + board[5] + " | " + board[6] + "        4 | 5 | 6");
        System.out.println("---+---+---      ---+---+---");
        System.out.println(" " + board[7] + " | " + board[8] + " | " + board[9] + "        7 | 8 | 9");
    }

    // Check if the current player has won
    public static boolean checkWinner() {
        for (int[] condition : winningConditions) {
            if (board[condition[1]].equals(currentPlayer) &&
                board[condition[2]].equals(currentPlayer) &&
                board[condition[3]].equals(currentPlayer)) {
                return true;
            }
        }
        return false;
    }

    // Check if the board is full (draw)
    public static boolean isDraw() {
        for (String cell : board) {
            if (cell.equals(" ")) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean gameActive = true;

        System.out.println("🎮 Welcome to Tic Tac Toe!");
        printBoard();

        while (gameActive) {
            System.out.println("Player " + currentPlayer + ", enter your move (0-8): ");
            int move = scanner.nextInt();

            if (move < 0 || move > 8 || !board[move].equals(" ")) {
                System.out.println("❌ Invalid move! Try again.");
                continue;
            }

            board[move] = currentPlayer;
            printBoard();

            if (checkWinner()) {
                System.out.println("🏆 Player " + currentPlayer + " wins!");
                gameActive = false;
            } else if (isDraw()) {
                System.out.println("🤝 It's a draw!");
                gameActive = false;
            } else {
                currentPlayer = currentPlayer.equals("X") ? "O" : "X";
            }
        }

        scanner.close();
    }
}