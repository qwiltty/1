https://github.com/qwiltty/1.gitfrom PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QFont
from conversion import *
import json

class Win1(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        self.current_question = 0
        self.connects()
        self.set_appear()
        self.show()
        self.questions_array = []
        self.save_questions_to_json()

    def InitUI(self):
        self.line_main = QVBoxLayout()
        
        self.line_h1 = QHBoxLayout()
        self.line_h2 = QHBoxLayout()
        self.line_h3 = QHBoxLayout()
        self.line_h4 = QHBoxLayout()
        self.line_h5 = QHBoxLayout()
        self.line_h6 = QHBoxLayout()
        self.line_h7 = QHBoxLayout()
        self.line_h8 = QHBoxLayout()
        self.line_h9 = QHBoxLayout()
        self.line_h10 = QHBoxLayout()
        self.line_h11 = QHBoxLayout()
        self.line_h12 = QHBoxLayout()
        self.line_h13 = QHBoxLayout()
        self.line_h14 = QHBoxLayout()
        self.line_h15 = QHBoxLayout()
        self.line_h9_1 = QHBoxLayout()
        self.line_h9_2 = QHBoxLayout()


        self.label1 = QLabel('Вопрос № 1')
        self.label1.setFont(QFont("Areal", 12, QFont.Bold))
        self.label2 = QLabel('Ваш вопрос:')
        self.label2.setFont(QFont("Times New Roman", 12, QFont.Bold))
        self.label3 = QLabel('Ответ 1:')
        self.label3.setFont(QFont("Times New Roman", 12))
        self.label4 = QLabel('Ответ 2:')
        self.label4.setFont(QFont("Times New Roman", 12))
        self.label5 = QLabel('Ответ 3:')
        self.label5.setFont(QFont("Times New Roman", 12))
        self.label6 = QLabel('Ответ 4:')
        self.label6.setFont(QFont("Times New Roman", 12))
        self.line_edit_main = QLineEdit()
        self.line_edit_main.setFont(QFont("Times New Roman", 12))
        self.line_edit1 = QLineEdit()
        self.line_edit1.setFont(QFont("Times New Roman", 12))
        self.line_edit2 = QLineEdit()
        self.line_edit2.setFont(QFont("Times New Roman", 12))
        self.line_edit3 = QLineEdit()
        self.line_edit3.setFont(QFont("Times New Roman", 12))
        self.line_edit4 = QLineEdit()
        self.line_edit4.setFont(QFont("Times New Roman", 12))
        self.label7 = QLabel('Правильный ответ под номером:')
        self.label7.setFont(QFont("Times New Roman", 12, QFont.Bold))

        self.button = QPushButton('Записать')
        self.button.setFont(QFont("Times New Roman", 12))
        self.button2 = QPushButton('Завершить')
        self.button2.setFont(QFont("Times New Roman", 12))
        self.buttonR1 = QRadioButton('1')
        self.buttonR1.setFont(QFont("Times New Roman", 12))
        self.buttonR2 = QRadioButton('2')
        self.buttonR2.setFont(QFont("Times New Roman", 12))
        self.buttonR3 = QRadioButton('3')
        self.buttonR3.setFont(QFont("Times New Roman", 12))
        self.buttonR4 = QRadioButton('4')
        self.buttonR4.setFont(QFont("Times New Roman", 12))
        
        self.line_h1.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.line_h2.addWidget(self.label2, alignment=Qt.AlignVCenter)
        
        self.line_h3.addWidget(self.line_edit_main, alignment=Qt.AlignVCenter)
        self.line_h4.addWidget(self.label3, alignment=Qt.AlignVCenter)

        self.line_h5.addWidget(self.line_edit1, alignment=Qt.AlignVCenter)
        self.line_h6.addWidget(self.label4, alignment=Qt.AlignVCenter)
        self.line_h7.addWidget(self.line_edit2, alignment=Qt.AlignVCenter)
        self.line_h8.addWidget(self.label5, alignment=Qt.AlignVCenter)
        self.line_h9.addWidget(self.line_edit3, alignment=Qt.AlignVCenter)
        self.line_h10.addWidget(self.label6, alignment=Qt.AlignVCenter)
        self.line_h9_1.addWidget(self.line_edit4, alignment=Qt.AlignVCenter)
        self.line_h9_2.addWidget(self.label7, alignment=Qt.AlignVCenter)
        self.line_h11.addWidget(self.buttonR1, alignment=Qt.AlignLeft)
        self.line_h12.addWidget(self.buttonR2, alignment=Qt.AlignLeft)
        self.line_h13.addWidget(self.buttonR3, alignment=Qt.AlignLeft)
        self.line_h14.addWidget(self.buttonR4, alignment=Qt.AlignLeft)
        self.line_h15.addWidget(self.button, alignment=Qt.AlignCenter)
        self.line_h15.addWidget(self.button2, alignment=Qt.AlignCenter)

        self.line_main.addLayout(self.line_h1)
        self.line_main.addLayout(self.line_h2)
        self.line_main.addLayout(self.line_h3)
        self.line_main.addLayout(self.line_h4)
        self.line_main.addLayout(self.line_h5)
        self.line_main.addLayout(self.line_h6)
        self.line_main.addLayout(self.line_h7)
        self.line_main.addLayout(self.line_h8)
        self.line_main.addLayout(self.line_h9)
        self.line_main.addLayout(self.line_h10)
        self.line_main.addLayout(self.line_h9_1)
        self.line_main.addLayout(self.line_h9_2)
        self.line_main.addLayout(self.line_h11)
        self.line_main.addLayout(self.line_h12)
        self.line_main.addLayout(self.line_h13)
        self.line_main.addLayout(self.line_h14)
        self.line_main.addLayout(self.line_h15)

        self.setLayout(self.line_main)
        
    
    def next_click(self):
        questions_dict = {}
        text_quest = self.line_edit_main.text()
        questions_dict['question'] = text_quest

        text_answer1 = self.line_edit1.text()
        questions_dict['answer1'] = text_answer1

        text_answer2 = self.line_edit2.text()
        questions_dict['answer2'] = text_answer2

        text_answer3 = self.line_edit3.text()
        questions_dict['answer3'] = text_answer3

        text_answer4 = self.line_edit4.text()
        questions_dict['answer4'] = text_answer4

        if self.buttonR1.isChecked():
            questions_dict['correct_answer'] = 'answer1'
        elif self.buttonR2.isChecked():
            questions_dict['correct_answer'] = 'answer2'
        elif self.buttonR3.isChecked():
            questions_dict['correct_answer'] = 'answer3'
        elif self.buttonR4.isChecked():
            questions_dict['correct_answer'] = 'answer4'

        self.questions_array.append(questions_dict)
        self.current_question += 1

        self.label1.setText('Вопрос № ' + str(self.current_question + 1))

        self.line_edit_main.clear()
        self.line_edit1.clear()
        self.line_edit2.clear()
        self.line_edit3.clear()
        self.line_edit4.clear()
    
    def next_click2(self):
        self.save_questions_to_json()
        self.hide()
        self.tw = Win2()

    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.button2.clicked.connect(self.next_click2)


    def set_appear(self):
        self.setWindowTitle('База викторины')
        self.resize(1400, 900)

    def save_questions_to_json(self):
        with open('bd_question.json', 'w', encoding='utf-8') as file:
            json.dump(self.questions_array, file, ensure_ascii=False, indent=4)

