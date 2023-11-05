# Файл с классами

class Form:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.correct = 0
        self.incorrect = 0
        self.all_ans = 0
        self.need_to_show = True

    def got_right(self):
        print("Правильно!")
        self.correct += 1
        self.all_ans += 1

    def got_wrong(self):
        print("Неправильно")
        self.incorrect += 1
        self.all_ans += 1

class FormView:
    def __init__(self, frm_model, question_W, answer_W, wrong_answer1_W, wrong_answer2_W, wrong_answer3_W):
        self.frm_model = frm_model
        self.question_W = question_W
        self.answer_W = answer_W
        self.wrong_answer1_W = wrong_answer1_W
        self.wrong_answer2_W = wrong_answer2_W
        self.wrong_answer3_W = wrong_answer3_W

    def setModel(self, frm_model):
        self.frm_model = frm_model

    def show(self):
        self.question_W.setText(self.frm_model.question)
        self.answer_W.setText(self.frm_model.answer)
        self.wrong_answer1_W.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2_W.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3_W.setText(self.frm_model.wrong_answer3)