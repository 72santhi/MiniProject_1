class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        #Displays the current board whenever the function is called
        print("-"*23)
        print("|R\\C|  0  |  1  |  2  |")
        for i in range(0, 3):
            print("-"*23)
            print(f"| {i} |  {self.board[i][0]}  |  {self.board[i][1]}  |  {self.board[i][2]}  |")
        print("-"*23)
        return -1
    
class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "X"
        self.moves = 0

    def switchPlayer(self):
        #Switch player
        self.turn = "O" if self.turn == "X" else "X" 

    def validateEntry(self, r, c):
        if not (0 <= r < 3) or not (0 <= c < 3):    
            print("Invalid entry: try again.")
            print("Row & column numbers must be either 0, 1 or 2.") 
            return 0
    
        #Validates if the cell is empty
        if self.board.board[r][c] != " ":
            print("That cell is already taken.")
            print("Please make another selection.") 
            return 0
        
        return 1
    
    def checkFull(self):
        return self.moves == 9

    def checkWin(self):
        """
        Checks if the current player has won the game.
        Scans rows, columns, and diagonals for four consecutive cells of the player's symbol.
        Returns:
            int: 1 if the player has won, 0 otherwise.
        """
        #row & column check
        for i in range(0, 3):
            if (self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] == self.turn):
                return 1
            if (self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i] == self.turn):
                return 1
            
        #diagnol check    
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] == self.turn:
            return 1
        if self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] == self.turn:
            return 1
        
        return 0   

    def checkEnd(self):
        """ 
        CheckEnd(self) returns True if a game is over, otherwise, returns False. 
        """
        if self.checkWin():
            print(f"{self.turn} IS THE WINNER!!!")
            return True
        elif self.checkFull():
            print("DRAW! NOBODY WINS!")
            return True
        return False

    def playGame(self):
        """ plays tic-tac-toe game by calling other methods. """
        print("New Game: X goes first.\n")
        self.board.printBoard()

        while True:
            # Prompt the current player to make a move
            print(f"\n{self.turn}'s, turn.")
            print(f"Where do you want your {self.turn} placed?")
            print("Please enter row number and column number seperated by a comma.")
            r, c = map(int, input().split(","))
            print(f"You have entered row #{r} \n  \t  and column  #{c}")

            # Validate the input
            if not self.validateEntry(r, c):
                continue

            # Update the board with the player's move
            print("Thank you for your selection.")
            self.board.board[r][c] = self.turn
            self.moves += 1
            self.board.printBoard()

            # Check if the game has ended
            if self.checkEnd():
                break

            # Switch player for the next turn
            self.switchPlayer()


# Start the game
def main():
    repeat = "y"

    while repeat[0].lower() == "y":
        game = Game()
        game.playGame()
        repeat = input("\nAnother game? Enter Y or y for yes.\n")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()

