from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QFont
import json
import os

def first_power():
    if not os.path.isfile("bd_question.json"):
        session = [] 
        with open("bd_question.json", 'w') as file:
            json.dump(session, file)

first_power()

def read_json(filename):
    with open(filename, "r", encoding='utf-8') as file:
        questions = json.load(file)
    return questions

questions = read_json("bd_question.json")
class Win3(QWidget):
    def __init__(self):
        super().__init__()

        self.current_question = 0
        self.result = 0
        self.noresult = 0
        self.questions = read_json("bd_question.json")


        self.InitUI()
        self.connects()
        self.set_appear()
        self.show()

    def InitUI(self):
        self.line_v1 = QVBoxLayout()
        self.line_v2 = QVBoxLayout()
        self.line_main = QVBoxLayout()
        
        self.line_h1 = QHBoxLayout()
        self.line_h2 = QHBoxLayout()
        self.line_h3 = QHBoxLayout()
        self.line_h4 = QHBoxLayout()
        self.line_h5 = QHBoxLayout()

        self.button = QPushButton('Ответить')
        self.button.setFont(QFont("Times", 12))
        self.buttonR1 = QRadioButton()
        self.buttonR2 = QRadioButton()
        self.buttonR3 = QRadioButton()
        self.buttonR4 = QRadioButton()

        self.text_timer = QLabel(QTime(0, 0, 0).toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        self.label1 = QLabel('Вопрос № ' + str(self.current_question + 1))
        self.label1.setFont(QFont("Areal", 20, QFont.Bold))
        self.label1.setStyleSheet("color: rgb(0, 0, 0)") 
        self.label2 = QLabel(self.questions[self.current_question]['question'])
        self.label2.setFont(QFont("Times New Roman", 14, QFont.Bold))
        self.label2.setStyleSheet("color: rgb(0, 0, 0)") 
        self.label3 = QLabel('Верных ответов:')
        self.label3.setFont(QFont("Times New Roman", 20))
        self.label3.setStyleSheet("color: rgb(101, 219, 78)")
        self.label4 = QLabel('Неверных ответов:')
        self.label4.setFont(QFont("Times New Roman", 20))
        self.label4.setStyleSheet("color: rgb(214, 31, 31)")        
        self.label5 = QLabel()
        self.label6 = QLabel()
        
        self.buttonR1.setText(self.questions[self.current_question]['answer1'])
        self.buttonR1.setFont(QFont("Times New Roman", 12))
        self.buttonR1.setStyleSheet("color: rgb(0, 0, 0)") 
        self.buttonR2.setText(self.questions[self.current_question]['answer2'])
        self.buttonR2.setFont(QFont("Times New Roman", 12))
        self.buttonR2.setStyleSheet("color: rgb(0, 0, 0)") 
        self.buttonR3.setText(self.questions[self.current_question]['answer3'])
        self.buttonR3.setFont(QFont("Times New Roman", 12))
        self.buttonR3.setStyleSheet("color: rgb(0, 0, 0)") 
        self.buttonR4.setText(self.questions[self.current_question]['answer4'])
        self.buttonR4.setFont(QFont("Times New Roman", 12))
        self.buttonR4.setStyleSheet("color: rgb(0, 0, 0)") 

        self.line_v1.addWidget(self.label3, alignment=Qt.AlignTop)
        self.line_v1.addWidget(self.label4, alignment=Qt.AlignTop)

        self.line_v2.addWidget(self.text_timer, alignment=Qt.AlignVCenter)

        self.line_h1.addWidget(self.label1, alignment=Qt.AlignCenter)

        self.line_h2.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.line_h3.addWidget(self.buttonR1, alignment=Qt.AlignCenter)
        self.line_h3.addWidget(self.buttonR2, alignment=Qt.AlignCenter)

        self.line_h4.addWidget(self.buttonR3, alignment=Qt.AlignCenter)
        self.line_h4.addWidget(self.buttonR4, alignment=Qt.AlignCenter)

        self.line_h5.addWidget(self.button, alignment=Qt.AlignCenter)

        self.line_main.addLayout(self.line_v1)
        self.line_main.addLayout(self.line_h1)
        self.line_main.addLayout(self.line_h2)
        self.line_main.addLayout(self.line_h3)
        self.line_main.addLayout(self.line_h4)
        self.line_main.addLayout(self.line_h5)
        self.line_main.addLayout(self.line_v2)

        self.setLayout(self.line_main)
    
    def next_click(self): 
        if self.questions[self.current_question]['correct_answer'] == 'answer1' and self.buttonR1.isChecked():
            self.result += 1
            self.label3.setText('Верных ответов: ' + str(self.result))
        elif self.questions[self.current_question]['correct_answer'] == 'answer2' and self.buttonR2.isChecked():
            self.result += 1
            self.label3.setText('Верных ответов: ' + str(self.result))
        elif self.questions[self.current_question]['correct_answer'] == 'answer3' and self.buttonR3.isChecked():
            self.result += 1
            self.label3.setText('Верных ответов: ' + str(self.result))
        elif self.questions[self.current_question]['correct_answer'] == 'answer4' and self.buttonR4.isChecked():
            self.result += 1
            self.label3.setText('Верных ответов: ' + str(self.result))
        else:
            self.noresult += 1
            self.label4.setText('Неверных ответов: ' + str(self.noresult))

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.label1.setText('Вопрос №' + str(self.current_question + 1))
            self.label2.setText(self.questions[self.current_question]['question'])
            self.buttonR1.setText(self.questions[self.current_question]['answer1'])
            self.buttonR2.setText(self.questions[self.current_question]['answer2'])
            self.buttonR3.setText(self.questions[self.current_question]['answer3'])
            self.buttonR4.setText(self.questions[self.current_question]['answer4'])
        else:
            self.label3.hide()
            self.label1.setText(f'Количество правильных ответов: {self.result}')
            self.label1.setFont(QFont("Times New Roman", 36, QFont.Bold))
            self.label1.setStyleSheet("color: rgb(101, 219, 78)")
            self.label2.hide()
            self.line_h2.addWidget(self.label6, alignment=Qt.AlignCenter)
            self.label4.hide()
            self.text_timer.hide()
            self.buttonR1.hide()
            self.buttonR2.hide()
            self.buttonR3.hide()
            self.buttonR4.hide()
            self.button.hide()
            self.line_h3.addWidget(self.label5, alignment=Qt.AlignCenter)
            self.label5.setFont(QFont("Times New Roman", 36, QFont.Bold))
            self.label5.setStyleSheet("color: rgb(0, 0, 0)")




    def timer_test(self):
        global time
        time = QTime(0, 0, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(+1)
        self.text_timer.setText(time.toString("hh:mm:ss")[3:8])
        seconds = time.secsTo(QTime(0, 0, 0))
        self.label5.setText(f"Время прохождения в секундах: {int(-seconds)}")
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if self.current_question >= len(self.questions):
            self.timer.stop()


    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.timer_test()


    def set_appear(self):
        self.setWindowTitle('Викторина')
        self.resize(1300, 800)
    