#1) Підключи необхідні модулі (QtCore і QtWidgets та їхні елементи).
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)

class Question:
	def __init__(self,question, right_answer, w1,w2,w3):
		self.qustion = question
		self.right_answer = right_answer
		self.w1 = w1
		self.w2 = w2
		self.w3 = w3

question_list = [
    Question(
        "Який тип даних у Python є незмінним (immutable)?",
        "tuple",
        "list",
        "dict",
        "set"
    ),
    Question(
        "Що виведе print(type(5))?",
        "<class 'int'>",
        "<class 'str'>",
        "<class 'float'>",
        "<class 'number'>"
    ),
    Question(
        "Яке ключове слово використовується для створення функції в Python?",
        "def",
        "func",
        "function",
        "lambda"
    ),
    Question(
        "Який оператор використовується для перевірки рівності?",
        "==",
        "=",
        "===",
        "!="
    ),
    Question(
        "Яке значення має булевий тип False?",
        "False",
        "0",
        "None",
        "false"
    ),
    Question(
        "Як отримати довжину списку lst?",
        "len(lst)",
        "lst.length()",
        "count(lst)",
        "size(lst)"
    ),
    Question(
        "Що робить оператор 'break' у циклі?",
        "Перериває виконання циклу",
        "Переходить до наступної ітерації",
        "Завершує програму",
        "Пропускає помилку"
    ),
    Question(
        "Який метод додає елемент у кінець списку?",
        "append",
        "add",
        "insert",
        "push"
    ),
    Question(
        "Який результат виразу: 3 * 2 ** 2?",
        "12",
        "36",
        "10",
        "9"
    ),
    Question(
        "Яке значення повертає функція input()?",
        "str",
        "int",
        "float",
        "bool"
    )
]




#2) Створи об'єкт програми, вікно програми. Встанови заголовок і розміри.
app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(400, 250)

#3) Створи віджет питання та віджет кнопки «Відповідь».
lb_question = QLabel("Переклади англійською слово автомобіль")

rbtn_1 = QRadioButton("Option1")
rbtn_2 = QRadioButton("Option2")
rbtn_3 = QRadioButton("Option3")
rbtn_4 = QRadioButton("Option4")

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

RadioButtonGroup = QButtonGroup()
RadioButtonGroup.addButton(rbtn_1)
RadioButtonGroup.addButton(rbtn_2)
RadioButtonGroup.addButton(rbtn_3)
RadioButtonGroup.addButton(rbtn_4)


btn_1 = QPushButton("Відповісти")


#4) Створи набір перемикачів з варіантами відповідей. Розмісти їх у макетах і об'єднай в групу.
 
lh_rbtn = QHBoxLayout()
lv_rbtn_1 = QVBoxLayout()
lv_rbtn_2 = QVBoxLayout()

lv_rbtn_1.addWidget(rbtn_1)
lv_rbtn_1.addWidget(rbtn_2)

lv_rbtn_2.addWidget(rbtn_3)
lv_rbtn_2.addWidget(rbtn_4)

lh_rbtn.addLayout(lv_rbtn_1)
lh_rbtn.addLayout(lv_rbtn_2)

RadioButtonGroupBox = QGroupBox("Варіанти відповідей")
RadioButtonGroupBox.setLayout(lh_rbtn)

# додали групу із відповідю 
AnswerGroup = QGroupBox("Відповідь")
lh_answerGroup = QHBoxLayout()
lb_answer = QLabel("Відповідь буде тут!")
lh_answerGroup.addWidget(lb_answer)
AnswerGroup.setLayout(lh_answerGroup)




 
#5) Розмісти питання, групу перемикачів і кнопку «Відповідь» у макетах.

main_layout = QVBoxLayout()

hl_1 = QHBoxLayout()
hl_2 = QHBoxLayout()
hl_3 = QHBoxLayout()

hl_1.addWidget(lb_question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
hl_2.addWidget(RadioButtonGroupBox)
hl_2.addWidget(AnswerGroup)

AnswerGroup.hide()

hl_3.addStretch(1)
hl_3.addWidget(btn_1, stretch=2)
hl_3.addStretch(1)

main_layout.addLayout(hl_1, stretch=1)
main_layout.addLayout(hl_2, stretch=8)

main_layout.addLayout(hl_3, stretch=2)


window.setLayout(main_layout)


def show_result(res):
	AnswerGroup.setTitle(res)
	btn_1.setText("Наступне питання")
	RadioButtonGroupBox.hide()
	AnswerGroup.show()


def show_question():
	btn_1.setText("Відповісти")
	RadioButtonGroupBox.show()
	AnswerGroup.hide()
	RadioButtonGroup.setExclusive(False)
	rbtn_1.setChecked(False)
	rbtn_2.setChecked(False)
	rbtn_3.setChecked(False)
	rbtn_4.setChecked(False)
	RadioButtonGroup.setExclusive(True)
 
def ask(question, right_answer, w1, w2, w3):
	shuffle(answers)
	answers[0].setText(right_answer)
	answers[1].setText(w1)
	answers[2].setText(w2)
	answers[3].setText(w3)
	lb_question.setText(question)
	lb_answer.setText(right_answer)
	show_question()

def check_answer():
	if btn_1.text() == "Відповісти":  
		if answers[0].isChecked():
			print("Correct")
			show_result("Правильно!")
		elif answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
			print("Incorrect")
			show_result("Ой-ой, ви зробили помилку!")
	elif btn_1.text() == "Наступне питання":
		show_question()
			
ask("Як буде 'машина' англійською?", "car", "home", "ask", "apple")

btn_1.clicked.connect(check_answer)

window.show()
app.exec_()
