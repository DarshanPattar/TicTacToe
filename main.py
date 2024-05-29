from actors import *

board = Board()

pen = input("Choose your sign, (x or o) : ")

if pen == "x":
    player = Player("x")
    computer = Computer("o")
elif pen == "o":
    player = Player("o")
    computer = Computer("x")
    computer.putInput(board)


board.display()

while not board.Conclusion:
    if not board.Conclusion:
        player.getInput(board)
        board.evaluate()
    if not board.Conclusion:
        computer.putInput(board)
        board.evaluate()
    board.display()
