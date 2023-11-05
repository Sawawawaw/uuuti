# Файл с интерфейсом основного окна

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])

menu_button = QPushButton("Меню")
rest_button = QPushButton("Відпочити")
ans_button = QPushButton("Відповісти")

rest_spinbox = QSpinBox()
rest_spinbox.setValue(30)

question_box = QGroupBox("Варіанти відповідей")
button_groupbox = QButtonGroup()
ans1_button = QRadioButton("")
ans2_button = QRadioButton("")
ans3_button = QRadioButton("")
ans4_button = QRadioButton("")

button_groupbox.addButton(ans1_button)
button_groupbox.addButton(ans2_button)
button_groupbox.addButton(ans3_button)
button_groupbox.addButton(ans4_button)

result_box = QGroupBox("Результати тестування")
question_label = QLabel("")
correct_label = QLabel("")

main_layout = QVBoxLayout()

head_layout = QHBoxLayout()
underhead_layout = QHBoxLayout()
question_layout = QHBoxLayout()
result_layout = QVBoxLayout()
footer_layout = QHBoxLayout()

column1_buttons = QVBoxLayout()
column2_buttons = QVBoxLayout()

head_layout.addWidget(menu_button, alignment=Qt.AlignLeft)
head_layout.addStretch(1)
head_layout.addWidget(rest_button, alignment=Qt.AlignRight)
head_layout.addWidget(rest_spinbox, alignment=Qt.AlignRight)

underhead_layout.addWidget(question_label, alignment=Qt.AlignCenter)

column1_buttons.addWidget(ans1_button)
column1_buttons.addWidget(ans2_button)
column2_buttons.addWidget(ans3_button)
column2_buttons.addWidget(ans4_button)

question_layout.addLayout(column1_buttons)
question_layout.addLayout(column2_buttons)

question_box.setLayout(question_layout)

result_layout.addWidget(question_label)
result_layout.addWidget(correct_label)

result_box.setLayout(result_layout)

footer_layout.addStretch(1)
footer_layout.addWidget(ans_button, stretch=2)
footer_layout.addStretch(1)

main_layout.addLayout(head_layout)
main_layout.addLayout(underhead_layout)
main_layout.addWidget(question_box)
main_layout.addWidget(result_box)
main_layout.addLayout(footer_layout)

def showAnswer():
    question_box.hide()
    result_box.show()
    ans_button.setText("Следующий вопрос")

def showQuestion():
    question_box.show()
    result_box.hide()
    ans_button.setText("Ответить")

