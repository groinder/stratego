import sys
from time import sleep

from PyQt5.QtWidgets import QApplication

from stratego.MinMax import MinMax
from stratego.MinMax2 import MinMax2
from stratego.MinMaxAB import MinMaxAB
from stratego.Stratego import Stratego
from stratego.StrategoUI import StrategoUI

size = 5

app = QApplication(sys.argv)
ui = StrategoUI(size)
app.processEvents()

stratego = Stratego(size)

minmax = MinMax2(2)
minmax_ab = MinMax2(2)

player1_points = 0
player2_points = 0

player1_turn = True
while not stratego.is_finished():
    if player1_turn:
        points, space, move_time = minmax.move(stratego)
        player1_points += points
        print("1", points, stratego.positions[space], move_time)
        ui.grid_place(stratego.positions[space], "1")
        ui.setPlayer1Points(player1_points)
    else:
        points, space, move_time = minmax_ab.move(stratego)
        player2_points += points
        print("2", points, stratego.positions[space], move_time)
        ui.grid_place(stratego.positions[space], "2")
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
