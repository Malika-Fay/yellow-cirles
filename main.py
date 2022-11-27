import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setFixedSize(400, 400)
        self.paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def run(self):
        self.paint = True
        self.repaint()

    def draw(self, qp):
        size = randrange(10, 100)
        place_y = randrange(60, 300)
        place_x = randrange(0, 300)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(place_x, place_y, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())