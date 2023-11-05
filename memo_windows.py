# Файл, где создали подокна меню и основной программі

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from menu_layout import form_layout
from main_layout import main_layout

wdgt_main = QWidget()
wdgt_menu = QWidget()

menu_layout = QVBoxLayout()
btn_layout = QHBoxLayout()

add_question = QPushButton("Добавить вопрос")
clear_button = QPushButton("Очистить поля")
main_button = QPushButton("Вернуться")

btn_layout.addWidget(add_question)
btn_layout.addWidget(clear_button)

menu_layout.addLayout(form_layout)
menu_layout.addLayout(btn_layout)
menu_layout.addWidget(main_button, alignment=Qt.AlignCenter)

wdgt_main.setLayout(main_layout)
wdgt_menu.setLayout(menu_layout)

layout_main = QVBoxLayout()
layout_main.addWidget(wdgt_main)
layout_main.addWidget(wdgt_menu)

# WINDOW (wdgt_main, wdgt_menu)