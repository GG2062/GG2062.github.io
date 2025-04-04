#Write a GUI program (class edition) to do the followings:
#•	Create a label to show “Welcome to Python” in green color in the top of the window.
#•	Create 3 buttons in red, blue and yellow colors to show “Hello!” in the position between the first label and buttons. 
#  Three buttons should be in the bottom of the window.
#•	Create a “Quit” button to exit the window
#•	Use different fonts and sizes

# importing tkinter
import tkinter

class My_GUI:

    # function to initialize the class. 
    def __init__(self):

        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create frames for top, buttons, and quit section.
        self.TFrame = tkinter.Frame(self.main_window)
        self.BFrame = tkinter.Frame(self.main_window)
        self.QuitFrame = tkinter.Frame(self.main_window)

        # Create the top label.
        self.label = tkinter.Label(self.TFrame, text = 'Welcome to Python!',\
                    fg = 'green', font = 'Times 40 bold')
        
        # Create button in the bottom of the window. 
        self.myBtn1 = tkinter.Button(self.BFrame, text = 'Hello!',\
                    fg = 'red', font = 'Helvetica 30', command = self.method1)
        self.myBtn2 = tkinter.Button(self.BFrame, text = 'Hello!',\
                    fg = 'blue', font = 'Phosphate 30 italic', command = self.method2)
        self.myBtn3 = tkinter.Button(self.BFrame, text = 'Hello!',\
                    fg = 'yellow', font = 'Couriernew 30 italic', command = self.method3)
        
        # Create the quit button.
        self.QuitBtn = tkinter.Button(self.QuitFrame, text = 'Quit',\
                    fg = 'purple', font = 'Times 30 bold', command = self.main_window.destroy)
        
        # Display the Label and button.
        self.label.pack()
        self.myBtn1.pack(side = 'left', ipadx = 10, ipady = 10, \
                        padx = 10, pady = 10)
        self.myBtn2.pack(side = 'left', ipadx = 10, ipady = 10, \
                        padx = 10, pady = 10)
        self.myBtn3.pack(side = 'left', ipadx = 10, ipady = 10, \
                        padx = 10, pady = 10)
        self.QuitBtn.pack()

        # pack frames
        self.TFrame.pack()
        self.BFrame.pack()
        self.QuitFrame.pack()

        # main loop to run multiples times.
        tkinter.mainloop()

    # method1
    def method1(self):
        self.myBtn1.config(text='Hello!', fg='red', font='Aptos 30 bold')

    # method2
    def method2(self):
        self.myBtn2.config(text='Hello!', fg='blue', font='Ayuthaya 40 bold')

    # method3
    def method3(self):
        self.myBtn3.config(text='Hello!', fg='yellow', font='Britannic 20 bold italic')

mygui = My_GUI()