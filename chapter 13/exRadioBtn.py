# exRadioBtn.py

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.rate = 10
        self.total = 0

        self.main_window = tkinter.Tk()

        self.TFrame = tkinter.Frame(self.main_window)
        self.BFrame = tkinter.Frame(self.main_window)

        self.radioVar = tkinter.IntVar(value = 1)
        #self.radioVar.set(1)

        self.rb1 = tkinter.Radiobutton(self.TFrame, text = 'Option 1', variable = self.radioVar, \
                value = 1, command = self.method1)
        
        self.rb2 = tkinter.Radiobutton(self.TFrame, text = 'Option 2', variable = self.radioVar, \
                value = 2, command = self.method2)
        
        self.rb3 = tkinter.Radiobutton(self.TFrame, text = 'Option 3', variable = self.radioVar, \
                value = 3, command = self.method3)
        
        self.okBtn = tkinter.Button(self.BFrame, text = 'OK', command = self.showResult)

        self.QuitBtn = tkinter.Button(self.BFrame, text = 'Quit', command = self.main_window.destroy)

        self.TFrame.pack()
        self.BFrame.pack()

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.okBtn.pack(side = 'left')
        self.QuitBtn.pack(side = 'left')

        tkinter.mainloop()

    def method1(self):
        self.rate = 10

    def method2(self):
        self.rate = 20

    def method3(self):
        self.rate = 40

    def showResult(self):
        self.total = 40 * self.rate
        tkinter.messagebox.showinfo('Total', f'Your total is ${self.total}.')

myqui = MyGUI()












