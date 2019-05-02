from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QApplication, QLabel

from stratego.StrategoGrid import StrategoGrid


class StrategoUI(QWidget):
    def on_size_change(self):
        new_size = int(self.size_input.text())
        self.grid.set_size(new_size)

    def __init__(self, size=4):
        super(StrategoUI, self).__init__()
        self.layout = QVBoxLayout()

        input_row = QHBoxLayout()
        self.size_input = QLineEdit()
        self.size_input.setValidator(QIntValidator())
        self.size_input.setText(str(size))
        input_row.addWidget(self.size_input)
        self.layout.addItem(input_row)

        points_row = QHBoxLayout()
        self.player1Label = QLabel("0")
        self.player2Label = QLabel("2")
        points_row.addWidget(self.player1Label)
        points_row.addWidget(self.player2Label)
        self.layout.addItem(points_row)

        self.grid = StrategoGrid(size)

        set_size_button = QPushButton("Set size")
        set_size_button.clicked.connect(self.on_size_change)
        input_row.addWidget(set_size_button)

        self.grid.layout.setParent(self.layout)
        self.layout.addItem(self.grid.layout)

        self.setLayout(self.layout)
        self.show()

    def grid_place(self, space, text):
        self.grid.place(space, text)

    def setPlayer1Points(self, points):
        self.player1Label.setText(str(points))

    def setPlayer2Points(self, points):
        self.player2Label.setText(str(points))
