from ast import Lambda
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import pywhatkit
import time
import pyautogui
import keyboard as k
import datetime
from PyQt5 import QtTest, QtWidgets
now = datetime.datetime.now()
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtCore import QTimer, QTime, Qt
import schedule
import sys
from datetime import datetime


class MainWindow(qtw.QTabWidget):
    def __init__(self):
        super().__init__()
        

#-------------Window Setup
        self.setWindowTitle("WhatsAuto")
        self.setMinimumSize(QSize(470, 300)) 
        self.setStyleSheet("background-color: #dcf8c6;")

        
#--------------Form Setup
        form_layout = qtw.QFormLayout()
        

        #Logo
        font = QtGui.QFont("Anton" , 20)
        label_1= qtw.QLabel("WHAT'S AUTO")
        font.setLetterSpacing(font.AbsoluteSpacing, 20)
        label_1.setFont(font)
        label_1.setAlignment(Qt.AlignCenter)
        label_1.setStyleSheet("border :3px ;background-color: #075e54; border-radius: 30px;color: #dcf8f6;")
        font_logo = label_1.font()
        

        
        
        #Message Box
        self.MessageEd = QLineEdit()
        self.MessageEd.setStyleSheet("QLineEdit {  border: 2px solid green;" "border-radius: 7px;background-color: solid white;padding :30px ;}")
        Message= qtw.QLabel("Message")
        self.MessageEd.setFixedHeight(20)
        Message.setFont(qtg.QFont("Helvetica", 15))


        self.NumberEd = QLineEdit()
        self.NumberEd.setStyleSheet("QLineEdit {  border: 2px solid green;" "border-radius: 7px;background-color: solid white;padding :30px ;}")
        Number= qtw.QLabel("Number")
        self.NumberEd.setFixedHeight(20)
        Number.setFont(qtg.QFont("Helvetica", 15))


        Minute= qtw.QLabel("Minutes")
        Hour= qtw.QLabel("Hour")
        Hour.setFont(qtg.QFont("Helvetica", 15))
        Minute.setFont(qtg.QFont("Helvetica", 15))

        my_combo = qtw.QSpinBox(self, maximum=24, minimum = 00)
        my_hour = qtw.QSpinBox(self, maximum=59, minimum = 00)
        layout = QHBoxLayout()
        layout.addWidget(my_combo)

        repLabel= qtw.QLabel("Repeat")
        repLabel.setFont(qtg.QFont("Helvetica", 15))
        repet = qtw.QComboBox(self)
        repet.addItem("0")
        repet.addItem("5")
        repet.addItem("10")
        repet.addItem("20")

        EveryLabel= qtw.QLabel("Every ? Minutes")
        EveryLabel.setFont(qtg.QFont("Helvetica", 15))
        every = qtw.QComboBox(self)
        every.addItem("2")
        every.addItem("5")
        every.addItem("10")
        every.addItem("30")

        pybutton = qtw.QPushButton('Send', self, clicked = lambda: press_it())
        pybutton.resize(100,32)
        pybutton.move(10, 350)
        pybutton.setStyleSheet("border-radius : 10; border : 2px solid green")

        #Form Layout
        form_layout.addRow(label_1)
        form_layout.addRow(Message, self.MessageEd)
        form_layout.addRow(Number, self.NumberEd)
        form_layout.addRow(repLabel, repet)
        form_layout.addRow(EveryLabel, every)
        form_layout.addRow(Hour,my_combo)
        form_layout.addRow(Minute,my_hour)
        
        
        #Buttons
        Send = qtw.QPushButton("Send", clicked = lambda: press_it())
        Send.resize(100,32)
        Send.move(50, 50)  
        self.layout().addWidget(Send)
        
        #Form Layout
        form_layout.addRow(pybutton)
        
        
        self.setLayout(form_layout)
     

#-----------------
        self.timer=QTimer()
        
        




        



        
        

        

#-----------------------------------FUNCTIONS
        
        def press_it():
            
            QtTest.QTest.qWait(int(duration()))
            pywhatkit.sendwhatmsg_instantly(str(self.NumberEd.text()), str(self.MessageEd.text()), 15, tab_close=True, close_time=2)

  
            content = repet.currentText()

            
            x=0
            while x < int(content):
      
                QtTest.QTest.qWait(int(every.currentText())*60000)
                pywhatkit.sendwhatmsg_instantly(str(self.NumberEd.text()), str(self.MessageEd.text()), 15, tab_close=True, close_time=5)
                print("vrai")
                x=x+1

            
        
        def duration():
            time=QDateTime.currentDateTime()
            start_time = time.toString('hh:mm:ss')
            end_time = f"{my_combo.value()}"":"f"{my_hour.value()}"":""00"
            t1 = datetime.strptime(start_time, "%H:%M:%S")
            t2 = datetime.strptime(end_time, "%H:%M:%S")
            delta = t2 - t1
            finalMs = delta.total_seconds() * 1000
            print(t1)
            print(t2)
            return finalMs
    
        

#--------------------------show the window

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
