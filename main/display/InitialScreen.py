from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
from main.display.Conversation import GameStart

os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'SNOW RUN'
        self.left = 50
        self.top = 200
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap('drawable/bkgd_winter1.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.titleLabel = QLabel(self)
        self.titleLabel.setText("< SNOW RUN >")
        self.titleLabel.setFont(QFont("궁서", 35))
        self.titleLabel.setStyleSheet("Color : black")
        self.titleLabel.move(240, 90)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("User Name:")
        self.nameLabel.setFont(QFont("궁서", 20))
        self.nameLabel.setStyleSheet("Color : black")
        self.nameLabel.move(40, 550)

        self.nameEdit = QLineEdit(self)
        self.nameEdit.setFont(QFont("궁서", 20))
        self.nameEdit.move(290, 550)

        self.startBtn = QPushButton(self)
        self.startBtn.setText("Start")
        self.startBtn.setFont(QFont("궁서", 23))
        self.startBtn.move(770, 545)
        # if self.startBtn.click():
        #     self.startBtn.clicked().connect(self.startBtnClicked())

    def startBtnClicked(self):
        self.jumpToCov = GameStart()
        self.jumpToCov.runThis()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    if ex.startBtn.click():
        ex.startBtnClicked()
    sys.exit(app.exec_())