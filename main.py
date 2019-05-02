import sys

from PyQt5.QtWidgets import QApplication

from stratego.MinMax import MinMax
from stratego.Stratego import Stratego
from stratego.StrategoUI import StrategoUI

size = 3

app = QApplication(sys.argv)
ui = StrategoUI(size)


stratego = Stratego(size)

minmax = MinMax()
minmax2 = MinMax()

player1_points = 0
player2_points = 0

player1_turn = True
while not stratego.is_finished():
    if player1_turn:
        points, space, move_time = minmax.move(stratego)
        player1_points += points
        print("1", points, space, move_time)
        ui.grid_place(space, "1")
        ui.setPlayer1Points(player1_points)
    else:
        points, space, move_time = minmax2.move(stratego)
        player2_points += points
        print("2", points, space, move_time)
        ui.grid_place(space, "2")
        ui.setPlayer2Points(player2_points)

    app.processEvents()
    player1_turn = not player1_turn

print("Player 1: ", player1_points)
print("Player 2: ", player2_points)

if player1_points > player2_points:
    print("Player 1 Wins")
else:
    print("Player 2 Wins")


app.exec_()
