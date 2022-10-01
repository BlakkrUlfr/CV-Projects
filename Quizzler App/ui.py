from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window_obj = Tk()

        self.window_obj.title('Quizzler')
        self.window_obj.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label_obj = Label(text='', fg='white', bg=THEME_COLOR)
        self.score_label_obj.grid(row=0, column=1)

        self.canvas_obj = Canvas(width=300, height=300, bg='white')

        self.canvas_text = self.canvas_obj.create_text((150, 150),
                                                       text='',
                                                       fill=THEME_COLOR,
                                                       font=('arial', 20, 'italic'),
                                                       width=290)

        self.canvas_obj.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window_obj.mainloop()

    def get_next_question(self):

        if self.quiz.still_has_questions():

            self.canvas_obj.config(bg='white')

            self.score_label_obj.config(text=f'Score: {self.quiz.score}')

            question_format = self.quiz.next_question()

            self.canvas_obj.itemconfig(self.canvas_text, text=question_format)

        elif not self.quiz.still_has_questions():

            self.canvas_obj.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")

            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):

        self.give_feedback(is_correct=self.quiz.check_answer('True'))

    def false_pressed(self):

        self.give_feedback(is_correct=self.quiz.check_answer('False'))

    def give_feedback(self, is_correct):

        if is_correct:

            self.canvas_obj.config(bg='green')

            self.window_obj.after(ms=1000, func=self.get_next_question)

        elif not is_correct:

            self.canvas_obj.config(bg='red')

            self.window_obj.after(ms=1000, func=self.get_next_question)


