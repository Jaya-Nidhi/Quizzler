from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Gui:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background= THEME_COLOR, padx=20, pady=20)

        self.Score_label = Label(text="Score=0", highlightthickness=0, foreground="white", background=THEME_COLOR)
        self.Score_label.grid(row=0, column=2)


        self.canvas = Canvas(width=300, height= 250)
        self.question_text = self.canvas.create_text(150,125,width=280,text = "question",
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)


        self.true =PhotoImage(file= "images/true.png")
        self.right= Button(image= self.true,highlightthickness=0, command=self.right)
        self.right.grid(row=4, column=1)


        self.false = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.false,highlightthickness=0, command=self.wrong )
        self.wrong.grid(row=4, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():

            self.Score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def right(self):
         self.give_feedback(self.quiz.check_answer("True"))
    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

