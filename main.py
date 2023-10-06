import random
import tkinter as tk
from tkinter import ttk
import json


class General(tk.Toplevel):
    def __init__(self, parent):

        with open("GeneralQ.json") as f:
            self.question = json.load(f)

        self.ans = [answer[0] for answer in self.question.values()]

        self.qna = {}

        for k, v in self.question.items():
            self.qna[k] = v[0]

        self.randQ = list(self.qna.keys())
        random.shuffle(self.randQ)
        self.randQ = random.sample(self.randQ, 25)

        self.options = list(self.question.values())
        super().__init__(parent)

        self.missed = []

        self.app = parent
        self.attributes("-fullscreen", True)
        self.title('General Questions Quiz')

        self.userAns = tk.StringVar()
        self.userAns.set('None')
        self.userScore = tk.IntVar()
        self.userScore.set(0)
        self.currQ = 0

        self.nextButton = tk.Button(self, text="Next Question",
                                    command=self.nextQ, font="calibre 30 bold", pady=20)

        self.reset = tk.Button(self, text="Start Again",
                               command=self.resetQuiz,
                               font="calibre 17 bold", width=50, height=5)

        self.f1 = ttk.Frame(self)
        self.f1.pack(side=tk.TOP, fill=tk.X)

        self.backFrame = ttk.Frame(self)
        self.backFrame.place(relx=0, rely=1, anchor='sw')
        tk.Button(self.backFrame, text="Back",
                  command=self.back, font="calibre 25 bold", width=25).pack(side='left')

        self.startQuiz()

    def startQuiz(self):
        self.userScore.set(0)
        self.nextButton.pack()
        self.nextQ()
        if self.missed:
            self.missed = []  # Evil fix

    def nextQ(self):
        if self.currQ < len(self.randQ):
            self.checkAns()
            self.userAns.set("None")
            cQuestion = self.randQ[self.currQ]
            self.clearFrame()

            tk.Label(self.f1, text=f"{self.currQ + 1}: {cQuestion}", padx=15, pady=100, font="calibre 50 bold",
                     wraplength=1500).pack()
            opt = list(self.question[cQuestion])
            random.shuffle(opt)

            for option in opt:
                tk.Radiobutton(self.f1, text=option, variable=self.userAns, value=option, padx=28,
                               font="calibre 30 normal", wraplength=1800).pack()
            self.currQ += 1

            tk.Label(self.f1, text=f"Your score: {self.userScore.get()} / {len(self.randQ)}", padx=15,
                     font="calibre 20 normal").pack(
                anchor=tk.SE)
        else:
            self.nextButton.forget()
            self.checkAns()
            self.clearFrame()
            # Dynamically adjust font size based on number of questions
            fontSize = min(30, int(300/len(self.randQ)))
            output = "Reset?"
            ttk.Label(self.f1, text=output, font="calibre 100 bold", anchor=tk.CENTER, justify=tk.CENTER).pack()
            ttk.Label(self.f1, text="Thanks for Participating", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            ttk.Label(self.f1, text=f"Score: {self.userScore.get()}", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            ttk.Label(self.f1, text="Questions missed:", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            for q in self.missed:
                # Adjust font if quiz displays lots of questions
                tk.Label(self.f1, text=q, font=f"calibre {fontSize} bold").pack()

            self.reset.pack(anchor='center')

    def resetQuiz(self):
        self.currQ = 0
        self.userScore.set(0)
        self.reset.forget()
        self.startQuiz()

    def checkAns(self):
        cQuestion = self.randQ[self.currQ - 1]
        temp = self.userAns.get()
        if temp != "None" and temp == self.qna[cQuestion]:
            self.userScore.set(self.userScore.get() + 1)
        else:
            self.missed.append(cQuestion)

    def clearFrame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()

    def back(self):
        self.app.deiconify()
        self.destroy()


class Data(tk.Toplevel):
    def __init__(self, parent):

        with open("DataStrucQ.json") as f:
            self.question = json.load(f)

        self.ans = [answer[0] for answer in self.question.values()]

        self.qna = {}

        for k, v in self.question.items():
            self.qna[k] = v[0]

        self.randQ = list(self.qna.keys())
        random.shuffle(self.randQ)
        self.randQ = random.sample(self.randQ, 25)

        self.options = list(self.question.values())
        super().__init__(parent)

        self.missed = []

        self.app = parent
        self.attributes("-fullscreen", True)
        self.title('General Questions Quiz')

        self.userAns = tk.StringVar()
        self.userAns.set('None')
        self.userScore = tk.IntVar()
        self.userScore.set(0)
        self.currQ = 0

        self.nextButton = tk.Button(self, text="Next Question",
                                    command=self.nextQ, font="calibre 30 bold", pady=20)

        self.reset = tk.Button(self, text="Start Again",
                               command=self.resetQuiz,
                               font="calibre 17 bold", width=50, height=5)

        self.f1 = ttk.Frame(self)
        self.f1.pack(side=tk.TOP, fill=tk.X)

        self.backFrame = ttk.Frame(self)
        self.backFrame.place(relx=0, rely=1, anchor='sw')
        tk.Button(self.backFrame, text="Back",
                  command=self.back, font="calibre 25 bold", width=25).pack(side='left')

        self.startQuiz()

    def startQuiz(self):
        self.userScore.set(0)
        self.nextButton.pack()
        self.nextQ()
        if self.missed:
            self.missed = []  # Evil fix

    def nextQ(self):
        if self.currQ < len(self.randQ):
            self.checkAns()
            self.userAns.set("None")
            cQuestion = self.randQ[self.currQ]
            self.clearFrame()

            tk.Label(self.f1, text=f"{self.currQ + 1}: {cQuestion}", padx=15, pady=100, font="calibre 50 bold",
                     wraplength=1500).pack()
            opt = list(self.question[cQuestion])
            random.shuffle(opt)

            for option in opt:
                tk.Radiobutton(self.f1, text=option, variable=self.userAns, value=option, padx=28,
                               font="calibre 30 normal", wraplength=1800).pack()
            self.currQ += 1

            tk.Label(self.f1, text=f"Your score: {self.userScore.get()} / {len(self.randQ)}", padx=15,
                     font="calibre 20 normal").pack(
                anchor=tk.SE)
        else:
            self.nextButton.forget()
            self.checkAns()
            self.clearFrame()
            # Dynamically adjust font size based on number of questions
            fontSize = min(30, int(300/len(self.randQ)))
            output = "Reset?"
            ttk.Label(self.f1, text=output, font="calibre 100 bold", anchor=tk.CENTER, justify=tk.CENTER).pack()
            ttk.Label(self.f1, text="Thanks for Participating", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            ttk.Label(self.f1, text=f"Score: {self.userScore.get()}", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            ttk.Label(self.f1, text="Questions missed:", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            for q in self.missed:
                # Adjust font if quiz displays lots of questions
                tk.Label(self.f1, text=q, font=f"calibre {fontSize} bold").pack()

            self.reset.pack(anchor='center')

    def resetQuiz(self):
        self.currQ = 0
        self.userScore.set(0)
        self.reset.forget()
        self.startQuiz()

    def checkAns(self):
        cQuestion = self.randQ[self.currQ - 1]
        temp = self.userAns.get()
        if temp != "None" and temp == self.qna[cQuestion]:
            self.userScore.set(self.userScore.get() + 1)
        else:
            self.missed.append(cQuestion)

    def clearFrame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()

    def back(self):
        self.app.deiconify()
        self.destroy()


class Algorithms(tk.Toplevel):
    def __init__(self, parent):

        with open("Algorithms.json") as f:
            self.question = json.load(f)

        self.ans = [answer[0] for answer in self.question.values()]

        self.qna = {}

        for k, v in self.question.items():
            self.qna[k] = v[0]

        self.randQ = list(self.qna.keys())
        random.shuffle(self.randQ)
        self.randQ = random.sample(self.randQ, 10)

        self.options = list(self.question.values())
        super().__init__(parent)

        self.missed = []

        self.app = parent
        self.attributes("-fullscreen", True)
        self.title('General Questions Quiz')

        self.userAns = tk.StringVar()
        self.userAns.set('None')
        self.userScore = tk.IntVar()
        self.userScore.set(0)
        self.currQ = 0

        self.nextButton = tk.Button(self, text="Next Question",
                                    command=self.nextQ, font="calibre 30 bold", pady=20)

        self.reset = tk.Button(self, text="Start Again",
                               command=self.resetQuiz,
                               font="calibre 17 bold", width=50, height=5)

        self.f1 = ttk.Frame(self)
        self.f1.pack(side=tk.TOP, fill=tk.X)

        self.backFrame = ttk.Frame(self)
        self.backFrame.place(relx=0, rely=1, anchor='sw')
        tk.Button(self.backFrame, text="Back",
                  command=self.back, font="calibre 25 bold", width=25).pack(side='left')

        self.startQuiz()

    def startQuiz(self):
        self.userScore.set(0)
        self.nextButton.pack()
        self.nextQ()
        if self.missed:
            self.missed = []  # Evil fix

    def nextQ(self):
        if self.currQ < len(self.randQ):
            self.checkAns()
            self.userAns.set("None")
            cQuestion = self.randQ[self.currQ]
            self.clearFrame()

            tk.Label(self.f1, text=f"{self.currQ + 1}: {cQuestion}", padx=15, pady=100, font="calibre 50 bold",
                     wraplength=1500).pack()
            opt = list(self.question[cQuestion])
            random.shuffle(opt)

            for option in opt:
                tk.Radiobutton(self.f1, text=option, variable=self.userAns, value=option, padx=28,
                               font="calibre 30 normal", wraplength=1800).pack()
            self.currQ += 1

            tk.Label(self.f1, text=f"Your score: {self.userScore.get()} / {len(self.randQ)}", padx=15,
                     font="calibre 20 normal").pack(
                anchor=tk.SE)
        else:
            self.nextButton.forget()
            self.checkAns()
            self.clearFrame()
            # Dynamically adjust font size based on number of questions
            fontSize = min(20, int(300 / len(self.randQ)))
            output = "Reset?"
            ttk.Label(self.f1, text=output, font="calibre 100 bold", anchor=tk.CENTER, justify=tk.CENTER).pack()
            ttk.Label(self.f1, text="Thanks for Participating", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            ttk.Label(self.f1, text=f"Score: {self.userScore.get()}", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            ttk.Label(self.f1, text="Questions missed:", font="calibre 50 bold", anchor=tk.CENTER,
                      justify=tk.CENTER).pack()
            for q in self.missed:
                # Adjust font if quiz displays lots of questions
                tk.Label(self.f1, text=q, font=f"calibre {fontSize} bold", wraplength=1800).pack()

            self.reset.pack(anchor='center')

    def resetQuiz(self):
        self.currQ = 0
        self.userScore.set(0)
        self.reset.forget()
        self.startQuiz()

    def checkAns(self):
        cQuestion = self.randQ[self.currQ - 1]
        temp = self.userAns.get()
        if temp != "None" and temp == self.qna[cQuestion]:
            self.userScore.set(self.userScore.get() + 1)
        else:
            self.missed.append(cQuestion)

    def clearFrame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()

    def back(self):
        self.app.deiconify()
        self.destroy()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.title("Quiz App")

        genStart = tk.Button(self, text="General Quiz",
                             command=self.openGen,
                             font="calibre 17 bold", width=50, height=5)

        genStart.pack(side='left', expand=True)

        dataStart = tk.Button(self, text="Data Structures Quiz",
                              command=self.openDS,
                              font="calibre 17 bold", width=50, height=5)

        dataStart.pack(side='left', expand=True)

        algoStart = tk.Button(self, text="Algorithm Quiz",
                              command=self.openAl,
                              font="calibre 17 bold", width=50, height=5)

        algoStart.pack(side="bottom", expand=True)

        ttk.Label(self, text='Choose a quiz', font="calibre 40 normal").place(relx=.5, rely=0.2, anchor='center')

        self.backFrame = ttk.Frame(self)
        self.backFrame.place(relx=0, rely=1, anchor='sw')
        tk.Button(self.backFrame, text="Close",
                  command=self.close, font="calibre 25 bold", width=25).pack(side='left')

    def openGen(self):
        newWindow = General(self)
        newWindow.grab_set()
        self.withdraw()

    def openDS(self):
        newWindow = Data(self)
        newWindow.grab_set()
        self.withdraw()

    def openAl(self):
        newWindow = Algorithms(self)
        newWindow.grab_set()
        self.withdraw()

    def close(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
