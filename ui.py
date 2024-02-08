from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#ABD1B5"
RED = "#B75D69"


class QuizInterface:
    """ For the front end : both appearance and functionalities """

    def __init__(self, quiz: QuizBrain):
        # class varaibles
        self.quiz = quiz
        self.window = Tk()
        # add app name and size
        self.window.title("Test Yourself")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # add score label
        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white", font=("Typewriter", 20, "italic"))
        self.score_label.grid(row=0, column=1)
        # add canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Question : ",
                                                     fill=THEME_COLOR,
                                                     font=("Typewriter", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons
        trueImg = PhotoImage(file="images/true.png")
        falseImg = PhotoImage(file="images/false.png")
        self.true_button = Button(image=trueImg, highlightthickness=0, command=lambda: self.checkTF("True"))
        self.false_button = Button(image=falseImg, highlightthickness=0, command=lambda: self.checkTF("False"))
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.getNewQuestion()
        # to refresh program every now and then
        self.window.mainloop()

    # --------------------------------- FUNCTIONALITIES ---------------------------------------------
    def getNewQuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finished all the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def checkTF(self, answer: str):
        """Check if the user's answer is right or wrong"""
        self.giveFeedback(self.quiz.check_answer(answer))

    def giveFeedback(self, user_is_right):
        bg_color = GREEN if user_is_right else RED
        self.canvas.config(bg=bg_color)
        self.window.after(1000, self.getNewQuestion)
