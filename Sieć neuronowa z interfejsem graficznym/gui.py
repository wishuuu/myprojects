import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QInputDialog
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QSize, Qt, QLine, QPoint,QRect
import sys

from net_managment import create_net, load_data, train, test

class Net(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Neuron Net')
        self.setGeometry(500,500,700,300)
        self.setLayout(qtw.QVBoxLayout())
        layers=[]
        layers.append({})

        self.btn1 = QPushButton('Make Net', self)
        self.btn1.move(180, 210)
        self.btn1.clicked.connect(self.make_net)

        self.btn2 = QPushButton('Train', self)
        self.btn2.move(300, 210)
        self.btn2.clicked.connect(self.train_net)

        self.btn3 = QPushButton('Test', self)
        self.btn3.move(420, 210)
        self.btn3.clicked.connect(self.test_net)

        self.le = []

        self.circles = []

        self.path = QLineEdit(self)
        self.path.move(100, 210)
        self.path.resize(70,30)

        self.path_text = QLabel(self)
        self.path_text.move(120, 240)
        self.path_text.setText("Path")


        self.lr = QLineEdit(self)
        self.lr.move(20, 210)
        self.lr.resize(70,30)

        self.lr_text = QLabel(self)
        self.lr_text.move(20, 240)
        self.lr_text.setText("Learning rate")

        self.setWindowTitle('Input Dialog')
        self.map()

        self.show()


    def map(self):
        container=qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        self.currX=20


        #buttons
        add_net=qtw.QPushButton('+',self)
        add_net.move(10,10)
        add_net.clicked.connect(self.on_clicked)

        #add_net.clicked.connect(self.paintEvent)

        sub_net=qtw.QPushButton('-',self)
        sub_net.move(110,10)
        sub_net.clicked.connect(self.on_clicked_sub)

    def on_clicked_sub(self):
  
        self.circles[len(self.circles)-1].hide()
        self.circles.pop()
        self.currX -= 180

        self.le[len(self.le)-1].hide()
        self.le.pop()


    def on_clicked(self):
        self.circles.append(qtw.QLabel('',self))
        self.circles[len(self.circles)-1].resize(80,80)
        self.circles[len(self.circles)-1].setStyleSheet("border: 3px solid black;border-radius: 40px;") 
        self.circles[len(self.circles)-1].move(self.currX,100)
        self.currX=self.currX+180
        self.circles[len(self.circles)-1].show()

        self.le.append(QLineEdit(self))
        self.le[len(self.le)-1].move(-141 + len(self.le) * 181, 50)
        self.le[len(self.le)-1].resize(35,30)
        self.le[len(self.le)-1].show()

    def make_net(self):
        layers = []
        for idx in range(len(self.le) - 1):
            layers.append({})
            layers[idx]['input'] = int(self.le[idx].text())
            layers[idx]['output'] = int(self.le[idx+1].text())
        learning_rate = float(self.lr.text())

        self.net = create_net(layers, learning_rate)

    def test_net(self):
        path = self.path.text()
        X, y = load_data(path)
        cost, acc = test(self.net, X, y)

        print("Cost: " + str(cost))
        print("Accuracy: " + str(acc))

    def train_net(self):
        path = self.path.text()
        X, y = load_data(path)
        train(self.net, X, y)

