from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import main.display.SelectConversation

os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Hello, Welcome to our Time Keeper'
        self.left = 50
        self.top = 200
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap('drawable/initialScreenBackground.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        titleLabel = QLabel(self)
        titleLabel.setText("Time Keeper")
        titleLabel.setFont(QFont("궁서",50))
        titleLabel.setStyleSheet("Color : white")
        titleLabel.move(375,70)

        nameLabel = QLabel(self)
        nameLabel.setText("User Name : ")
        nameLabel.setFont(QFont("궁서",20))
        nameLabel.setStyleSheet("Color : white")
        nameLabel.move(20,550)

        nameEdit = QLineEdit(self)
        nameEdit.setFont(QFont("궁서",20))
        nameEdit.move(210,550)

        startBtn = QPushButton(self)
        startBtn.setText("Start")
        startBtn.setFont(QFont("궁서",23))
        startBtn.move(600,546)

        #startBtn.clicked.connect(Selecct Class)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())