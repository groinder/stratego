from PyQt5.QtWidgets import QLabel, QGridLayout


class StrategoGrid:
    layout = QGridLayout()

    def refresh(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()

        for i in range(self.size):
            for j in range(self.size):
                widget = QLabel(" ")
                self.layout.addWidget(widget, i, j)

    def set_size(self, size):
        self.size = size
        self.refresh()

    def place(self, space, text):
        widget = QLabel(text)
        self.layout.replaceWidget(self.layout.itemAtPosition(space[0], space[1]).widget(), widget)

    def __init__(self, size=4):
        self.size = size
        self.refresh()
