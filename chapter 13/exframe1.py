
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.TFrame = tkinter.Frame(self.main_window)
        self.BFrame = tkinter.Frame(self.main_window)

        self.LT1 = tkinter.Label(self.TFrame, text = ' Tra', fg = 'blue', bg = 'red',\
                                 font = 'Times 20 bold italic')
        self.LT2 = tkinter.Label(self.TFrame, text = 'Grishma', fg = 'pink', bg = 'grey',\
                                 font = 'Helvetica 30 bold')
        self.LT3 = tkinter.Label(self.TFrame, text = 'Sandeep', fg = 'blue', bg = 'black',\
                                 font = 'Couriernew 25 underline')
        self.LT4 = tkinter.Label(self.TFrame, text = 'Alex')

        self.LB1 = tkinter.Label(self.BFrame, text = 'Issac')
        self.LB2 = tkinter.Label(self.BFrame, text = 'Raheem') 
        self.LB3 = tkinter.Label(self.BFrame, text = 'Quynh')

        self.LT1.grid(row = 1, column = 1)
        self.LT2.grid(row = 2, column = 3)
        self.LT3.grid(row = 3, column = 4)
        self.LT4.grid(row = 4, column = 2)

        self.LB1.grid(row = 3, column = 1)
        self.LB2.grid(row = 2, column = 3)
        self.LB3.grid(row = 1, column = 2)

        '''
        self.LT1.pack()
        self.LT2.pack()
        self.LT3.pack()
        self.LT4.pack()

        self.LB1.pack(side = 'left')
        self.LB2.pack(side = 'left')
        self.LB3.pack(side = 'left')
        '''
        
        self.TFrame.pack()
        self.BFrame.pack()
        
        tkinter.mainloop()

my_gui = MyGUI()
