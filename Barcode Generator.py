from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from barcode import *
import random
from barcode.writer import ImageWriter

import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        # Loading the created UI file in the class
        uic.loadUi("barcode.ui", self)
        # Setting title of the window
        self.setWindowTitle("Barcode Generator")

        self.choices = self.findChild(QComboBox,"formats")
        self.n = self.findChild(QLineEdit,"lineEdit")
        #pg1
        self.output1 = self.findChild(QLabel,"label_3")
        self.generate1 = self.findChild(QPushButton,"generator1")
        #pg2
        self.output2 = self.findChild(QLabel,"label_4")
        self.generate2 = self.findChild(QPushButton,"generator2")

        self.generate1.clicked.connect(self.upca)
        self.generate2.clicked.connect(self.isbn13)

        self.show()

    def isbn13(self):
        n = 11
        terms = []
        num = 0
        am = ""
        a_s = []
        sum_13 = []
        last_digit = 0
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, 10):
            a = random.choice(lst)
            a_s.append(a)
            n = n - 1
            term = a * n
            num = int(num) + int(term)
            am = am + str(a)

            terms.append(term)

        for i in range(0, 9):
            if i % 2 == 0:
                term = a_s[i] * 3
            else:
                term = a_s[i] * 1
            sum_13.append(term)
        sum13 = sum(sum_13) + 38
        check1 = int(sum13) % 10
        if check1 == 0:
            last_digit13 = 0
        else:
            last_digit13 = 10 - check1
        am13 = str(978) + am + str(last_digit13)
        number1 = am13
        my_code1 = UPCA(number1, writer=ImageWriter())
        my_code1.save("new_code2")
        self.n.setText(number1)
        pixmap = QPixmap('new_code2.png')
        self.output2.setPixmap(pixmap)

        print(am13)
    def upca(self):
        a_s = []
        e_sum = 0
        o_sum = 0
        num = ""
        for i in range(11):
            a = random.randint(0, 9)
            a_s.append(a)
        for k in range(11):
            if (k + 1) % 2 == 0:
                e_sum = e_sum + a_s[k]
            else:
                o_sum = o_sum + a_s[k]
        stp2 = o_sum * 3
        print(stp2)
        stp4 = stp2 + e_sum
        print(stp4)
        stp5 = (stp4) % 10
        print(stp5)
        check_digit = 10 - stp5
        print(check_digit)
        a_s.append(check_digit)
        print("as" + str(a_s))
        for i in a_s:
            num = num + str(i)
        print("num" + num)
        print(e_sum)
        print(o_sum)
        number = num
        print(number)
        my_code = UPCA(number, writer=ImageWriter())
        my_code.save("new_code1")
        self.n.setText(number)
        pixmap = QPixmap('new_code1.png')
        self.output1.setPixmap(pixmap)


app = QApplication(sys.argv)
UIWindow = mainwindow()
app.exec_()