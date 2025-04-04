# Write a GUI program (class edition) that displays your name and address when a button is clicked. 
# A Show Info button and a Quit button are created in the program.  When the user clicks the Show Info button, 
# the program should display your name and address. 
# When the user clicks the Quit button, the window will be closed.  (See the following Figure)

# importing tkinter
import tkinter

class MyGUI:

    # function to initialize the class. 
    def __init__(self):

        # Create the main window widget.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x300')

        # Frames
        self.TFrame = tkinter.Frame(self.main_window) 
        self.MFrame = tkinter.Frame(self.main_window) 
        self.BFrame = tkinter.Frame(self.main_window) 

        # Create show info button and quit button.
        self.myBtn = tkinter.Button(self.TFrame, text = 'Show Info!',\
                command = self.display)
        self.QuitBtn = tkinter.Button(self.BFrame, text = 'Quit',\
                command = self.main_window.destroy)
        self.dislabel = tkinter.Label(self.MFrame, text = '')
        
        # Display the button.
        self.myBtn.pack(side = 'left', ipadx = 20, ipady = 20, \
                        padx = 20, pady = 30)
        self.QuitBtn.pack(side = 'left', ipadx = 20, ipady = 20, \
                        padx = 20, pady = 30)
        self.dislabel.pack()

        self.TFrame.pack()
        self.MFrame.pack()
        self.BFrame.pack()
        # main loop to run multiples times.
        tkinter.mainloop()

    # display method
    def display(self):
        self.dislabel.config(text = 'Grishma Gurung \n Sheboygan, WI')

my_gui = MyGUI()