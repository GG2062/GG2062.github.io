# exColor1.py

import tkinter

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text = 'Hello World!',\
                    fg = 'blue', bg = 'red', font = 'Times 40 bold')
        
        self.button = tkinter.Button(self.main_window, text = 'Change Colors', \
                    fg = 'purple', bg = 'yellow', command = self.process)
        
        self.label.pack()
        self.button.pack()

        tkinter.mainloop()

    def process(self):
        self.label['fg'] = 'red'
        self.label['bg'] = 'green'
        self.label['text'] = 'Merry Christmas'
        self.label['font'] = 'Couriernew 80 bold'

mygui = My_GUI()
