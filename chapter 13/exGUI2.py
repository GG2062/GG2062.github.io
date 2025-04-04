# exGUI2.py

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('My First GUI')
        #self.main_window.geometry('500x300')

        self.label1 = tkinter.Label(self.main_window, text = 'Hello World!', \
                                    borderwidth = 1, relief = 'solid')
        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program', \
                                    borderwidth = 3, relief = 'groove')
        self.label3 = tkinter.Label(self.main_window, text = 'This is the third line', \
                                    borderwidth = 5, relief = 'sunken')

        '''
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        '''

        self.label1.pack(side = 'top', ipadx = 20, ipady = 20, \
                         padx = 20, pady = 30)
        self.label2.pack(side = 'bottom', ipadx = 20, ipady = 20, \
                         padx = 20, pady = 30)
        self.label3.pack(side = 'right', ipadx = 50, ipady = 50, \
                         padx = 50, pady = 50)

        tkinter.mainloop()

my_gui = MyGUI()



