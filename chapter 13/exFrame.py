# exFrame.py

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.TFrame = tkinter.Frame(self.main_window)
        self.BFrame = tkinter.Frame(self.main_window)

        self.LT1 = tkinter.Label(self.TFrame, text = ' Tra')
        self.LT2 = tkinter.Label(self.TFrame, text = 'Grishma')
        self.LT3 = tkinter.Label(self.TFrame, text = 'Sandeep')
        self.LT4 = tkinter.Label(self.TFrame, text = 'Alex')

        self.LB1 = tkinter.Label(self.TFrame, text = 'Issac')
        self.LB2 = tkinter.Label(self.TFrame, text = 'Raheem') 
        self.LB3 = tkinter.Label(self.TFrame, text = 'Quynh')

        self.LT1.pack()
        self.LT2.pack()
        self.LT3.pack()
        self.LT4.pack()

        self.LB1.pack(side = 'left')
        self.LB2.pack(side = 'left')
        self.LB3.pack(side = 'left')

        self.TFrame.pack()
        self.BFrame.pack()

        tkinter.mainloop()

my_gui = MyGUI()
