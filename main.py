import random
import tkinter as tk
from tkinter import ttk
import json


class General(tk.Toplevel):
    def __init__(self, parent):

        with open("GeneralQ.json") as f:
            self.question = json.load(f)

        self.ans = [answer[0] for answer in self.question.values()]

        self.options = list(self.question.values())
        super().__init__(parent)

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
        self.nextButton.pack()
        self.nextQ()

    def nextQ(self):
        if self.currQ < len(self.question):
            self.checkAns()
            self.userAns.set("None")
            cQuestion = list(self.question.keys())[self.currQ]
            self.clearFrame()

            tk.Label(self.f1, text=f"{self.currQ + 1}: {cQuestion}", padx=15, pady=100, font="calibre 50 bold").pack()
            opt = list(self.question[cQuestion])
            random.shuffle(opt)

            for option in opt:
                tk.Radiobutton(self.f1, text=option, variable=self.userAns, value=option, padx=28,
                               font="calibre 30 normal").pack()
            self.currQ += 1

            tk.Label(self.f1, text=f"Your score: {self.userScore.get()} / {len(self.question)}", padx=15,
                     font="calibre 20 normal").pack(
                anchor=tk.SE)
        else:
            self.nextButton.forget()
            self.checkAns()
            self.clearFrame()
            output = "Reset?"
            tk.Label(self.f1, text=output, font="calibre 25 bold").pack()
            tk.Label(self.f1, text="Thanks for Participating", font="calibre 18 bold").pack()

            self.reset.pack()

    def resetQuiz(self):
        self.currQ = 0
        self.userScore.set(0)
        self.reset.forget()
        self.startQuiz()

    def checkAns(self):
        temp = self.userAns.get()
        if temp != "None" and temp == self.ans[self.currQ - 1]:
            self.userScore.set(self.userScore.get() + 1)

    def clearFrame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()

    def back(self):
        self.app.deiconify()
        self.destroy()


class Data(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        with open("DataStrucQ.json") as f:
            self.question = json.load(f)

        self.ans = [answer[0] for answer in self.question.values()]

        self.options = list(self.question.values())

        self.app = parent
        self.attributes("-fullscreen", True)
        self.title('Data Structures Quiz')

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
        self.nextButton.pack()
        self.nextQ()

    def nextQ(self):
        if self.currQ < len(self.question):
            self.checkAns()
            self.userAns.set("None")
            cQuestion = list(self.question.keys())[self.currQ]
            self.clearFrame()

            tk.Label(self.f1, text=f"{self.currQ + 1}: {cQuestion}", padx=15, pady=100, font="calibre 50 bold").pack()
            opt = list(self.question[cQuestion])
            random.shuffle(opt)

            for option in opt:
                tk.Radiobutton(self.f1, text=option, variable=self.userAns, value=option, padx=28,
                               font="calibre 30 normal").pack()
            self.currQ += 1

            tk.Label(self.f1, text=f"Your score: {self.userScore.get()} / {len(self.question)}", padx=15,
                     font="calibre 20 normal").pack(
                anchor=tk.SE)
        else:
            self.nextButton.forget()
            self.checkAns()
            self.clearFrame()
            output = "Reset?"
            tk.Label(self.f1, text=output, font="calibre 25 bold").pack()
            tk.Label(self.f1, text="Thanks for Participating", font="calibre 18 bold").pack()

            self.reset.pack()

    def resetQuiz(self):
        self.currQ = 0
        self.userScore.set(0)
        self.reset.forget()
        self.startQuiz()

    def checkAns(self):
        temp = self.userAns.get()
        if temp != "None" and temp == self.ans[self.currQ - 1]:
            self.userScore.set(self.userScore.get() + 1)

    def clearFrame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()

    def back(self):
        self.app.deiconify()
        self.destroy()


class Algorithms(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        with open("Algorithms.json") as f:
            self.question = json.load(f)

        self.ans = [answer[0] for answer in self.question.values()]

        self.options = list(self.question.values())

        self.app = parent
        self.attributes("-fullscreen", True)
        self.title('Algorithms Quiz')

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
        self.nextButton.pack()
        self.nextQ()

    def nextQ(self):
        if self.currQ < len(self.question):
            self.checkAns()
            self.userAns.set("None")
            cQuestion = list(self.question.keys())[self.currQ]
            self.clearFrame()

            tk.Label(self.f1, text=f"{self.currQ + 1}: {cQuestion}", padx=15, pady=100, font="calibre 50 bold").pack()
            opt = list(self.question[cQuestion])
            random.shuffle(opt)

            for option in opt:
                tk.Radiobutton(self.f1, text=option, variable=self.userAns, value=option, padx=28,
                               font="calibre 30 normal").pack()
            self.currQ += 1

            tk.Label(self.f1, text=f"Your score: {self.userScore.get()} / {len(self.question)}", padx=15,
                     font="calibre 20 normal").pack(
                anchor=tk.SE)
        else:
            self.nextButton.forget()
            self.checkAns()
            self.clearFrame()
            output = "Reset?"
            tk.Label(self.f1, text=output, font="calibre 25 bold").pack()
            tk.Label(self.f1, text="Thanks for Participating", font="calibre 18 bold").pack()

            self.reset.pack()

    def resetQuiz(self):
        self.currQ = 0
        self.userScore.set(0)
        self.reset.forget()
        self.startQuiz()

    def checkAns(self):
        temp = self.userAns.get()
        if temp != "None" and temp == self.ans[self.currQ - 1]:
            self.userScore.set(self.userScore.get() + 1)

    def back(self):
        self.app.deiconify()
        self.destroy()

    def clearFrame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()


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
