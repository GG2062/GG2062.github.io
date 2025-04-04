# I.Write a GUI program (class edition) to develop a simple math calculator.  
# The user should be able to enter two numbers, and click one of four buttons to do the +, -, *, or / operations. 
# Then the program will display the result.
#  Note: if the divisor in the / operation is 0, display ‘N/A’ in the result.     

import tkinter

class MathCalGUI:

    # initializing
    def __init__(self):

        # Main window
        self.main_window = tkinter.Tk()

        # Frames 
        self.Tframe = tkinter.Frame(self.main_window)
        self.Bframe = tkinter.Frame(self.main_window)
        self.Mframe = tkinter.Frame(self.main_window)

        # Input fields and labels
        self.N1label = tkinter.Label(self.Tframe, text = 'Number 1: ')
        self.N1entry = tkinter.Entry(self.Tframe, width=10)
        self.N2label = tkinter.Label(self.Tframe, text='Number 2: ')
        self.N2entry = tkinter.Entry(self.Tframe, width=10)

        # Buttons for operations
        self.AddBtn = tkinter.Button(self.Bframe, text = '+', command = self.add)
        self.SubBtn = tkinter.Button(self.Bframe, text = '-', command = self.subtract)
        self.MulBtn = tkinter.Button(self.Bframe, text = '*', command = self.multiply)
        self.DivBtn = tkinter.Button(self.Bframe, text = '/', command = self.divide)
        self.QuitBtn = tkinter.Button(self.Bframe, text = 'Quit', command = self.main_window.destroy)

        # display the results
        self.resLabel = tkinter.Label(self.Mframe, text = 'Result: ')
        self.value = tkinter.StringVar()
        self.resDisplay = tkinter.Label(self.Mframe, textvariable = self.value)

        # Input pack
        self.N1label.pack(side='left')
        self.N1entry.pack(side='left')
        self.N2label.pack(side='left')
        self.N2entry.pack(side='left')

        # buttons pack
        self.AddBtn.pack(side='left')
        self.SubBtn.pack(side='left')
        self.MulBtn.pack(side='left')
        self.DivBtn .pack(side='left')
        self.QuitBtn.pack(side='left')

        # result pack
        self.resLabel.pack(side = 'left')
        self.resDisplay.pack(side='left')

        # Pack frames
        self.Tframe.pack()
        self.Mframe.pack()
        self.Bframe.pack()

        # the main loop
        tkinter.mainloop()

    # getmethod to get the two numbers from user
    def get_numbers(self):
        num1 = float(self.N1entry.get())
        num2 = float(self.N2entry.get())
        return num1, num2
        
    # add (+) operation method
    def add(self):
        num1, num2 = self.get_numbers()
        self.value.set(f'{num1 + num2:.1f}')

    # sub (-) operation method
    def subtract(self):
        num1, num2 = self.get_numbers()
        self.value.set(f'{num1 - num2:.1f}')

    # multiply (*) operation method
    def multiply(self):
        num1, num2 = self.get_numbers()
        self.value.set(f'{num1 * num2:.1f}')

    # divides (/) operation method
    def divide(self):
        num1, num2 = self.get_numbers()
        # if/else to check if num is 0.
        if num2 == 0:
            self.value.set('N/A')
        else:
            self.value.set(f'{num1 / num2:.2f}')

MCobj = MathCalGUI()
