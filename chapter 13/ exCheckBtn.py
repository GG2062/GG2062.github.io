# exCheckBtn.py

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.TFrame = tkinter.Frame(self.main_window)
        self.BFrame = tkinter.Frame(self.main_window)

        self.cbVar1 = tkinter.IntVar()
        self.cbVar2 = tkinter.IntVar()
        self.cbVar3 = tkinter.IntVar()
        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)

        self.cb1 = tkinter.Checkbutton(self.TFrame, text = 'Option 1', variable = self.cbVar1)
        self.cb2 = tkinter.Checkbutton(self.TFrame, text = 'Option 2', variable = self.cbVar2)
        self.cb3 = tkinter.Checkbutton(self.TFrame, text = 'Option 3', variable = self.cbVar3)

        self.okBtn = tkinter.Button(self.BFrame, text = 'OK', command = self.showResult)

        self.QuitBtn = tkinter.Button(self.BFrame, text = 'Quit', command = self.main_window.destroy)

        self.TFrame.pack()
        self.BFrame.pack()

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.okBtn.pack(side = 'left')
        self.QuitBtn.pack(side = 'left')

        tkinter.mainloop()

    def showResult(self):
        message = 'You selected: \n'

        if self.cbVar1.get() == 1:
            message += '1\n'

        if self.cbVar2.get() == 1:
            message += '2\n'

        if self.cbVar3.get() == 1:
            message += '3\n'

        tkinter.messagebox.showinfo('Selection', message)

mygui = MyGUI()


        