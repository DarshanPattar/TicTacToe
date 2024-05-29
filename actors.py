from difflib import SequenceMatcher
import random

class Board:
    def __init__(self):
        self.boardMap = [
            "n","n","n",
            "n","n","n",
            "n","n","n"
        ]
        self.winStrings = ["123", "456", "789", "147", "258", "369", "159", "357"]
        self.p1Moves = []
        self.p2Moves = []
        self.Conclusion = False
    
    def evaluate(self):
        p = self.p1Moves
        c = self.p2Moves
        
        playerMoves = set(p)
        computerMoves = set(c)

        for cond in self.winStrings:
            c = set(list(cond))
            if c.issubset(playerMoves):
                print("Player Wins")
                self.Conclusion = True
            
            if c.issubset(computerMoves):
                print("Computer Wins")
                self.Conclusion = True

    def display(self):
        for i, n in enumerate(self.boardMap):
            if n == "n":
                print("   ", end="")
            if n == "o":
                print(" o ", end="")
            if n == "x":
                print(" x ", end="")
            if (i + 1) % 3 == 0:
                print("\n", end="")
            else:
                print("|", end="")


class Player:

    def __init__(self, side):
        self.side = side

    def getInput(self, board):
        pen = input(">")
        board.p1Moves.append(pen)
        board.boardMap[int(pen)-1] = self.side


class Computer:

    def __init__(self, side):
        self.side = side
    
    
    def putInput(self, board):
        pen = self.getSquare(board)
        board.p2Moves.append(pen)
        board.boardMap[int(pen)-1] = self.side


    def getSquare(self, board):
        playerMoves = board.p1Moves
        computerMoves = board.p2Moves
        wins = board.winStrings

        taken = playerMoves + computerMoves

        playerMoves.sort()
        playerMoves = "".join(playerMoves)

        computerMoves.sort()
        computerMoves = "".join(computerMoves)
        
        for cond in wins:
            if self.similiar(computerMoves, cond) > 0.6:
                #print(computerMoves, cond)
                p = set(list(computerMoves))
                c = set(list(cond))
                n = c.difference(p)
                k = list(n)[0]
                if k not in taken:
                    return k
                
            if self.similiar(playerMoves, cond) > 0.6:
                #print(playerMoves, cond)
                p = set(list(playerMoves))
                c = set(list(cond))
                n = c.difference(p)
                k = list(n)[0]
                if k not in taken:
                    return k
        
        positions = set(['1', '2', '3', '4', '5' ,'6' ,'7', '8', '9'])
        available = positions.difference(set(taken))

        return random.choice(list(available))
        

    def similiar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

