# exBtn1.py

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.myBtn = tkinter.Button(self.main_window, text = 'Click me!',\
                                    command = self.do_something)
        self.QuitBtn = tkinter.Button(self.main_window, text = 'Quit',\
                                    command = self.main_window.destroy)
        self.myBtn.pack()
        self.QuitBtn.pack()

        tkinter.mainloop()

    #callback function
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for coming to the class today!')

my_gui = MyGUI()