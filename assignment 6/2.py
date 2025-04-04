# II.	Write a GUI program (class edition) containing radio buttons to calculate the cost of a computer with the options selected by the user.  Use the following information:
   		#Processor:  Intel Core i7 ($250), Intel Core i9 ($350)
    	#Memory: 16GB ($150), 32GB ($250)
    	#Hard drive:  512GB ($100), 1TB ($150), 2TB ($225)
    	#Monitor: 19” ($200), 21” ($300), 24” ($400)

import tkinter
import tkinter.messagebox

class MyGUI:
    
	# initializing
    def __init__(self):
        self.processorCost = 0
        self.memoryCost = 0
        self.hardDriveCost = 0
        self.monitorCost = 0
        self.total = 0

        # Main window
        self.main_window = tkinter.Tk()

        # Frames
        self.TFrame = tkinter.Frame(self.main_window)  
        self.BFrame = tkinter.Frame(self.main_window)  

        # Processor Options
        self.processorVar = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.TFrame, text = 'Intel Core i7 ($250)', variable = self.processorVar,\
                value = 250, command = self.set_processor1)
        self.rb2 = tkinter.Radiobutton(self.TFrame, text = 'Intel Core i9 ($350)', variable = self.processorVar,\
                value = 350, command = self.set_processor2)

        # Memory Options
        self.memoryVar = tkinter.IntVar()
        self.rb3 = tkinter.Radiobutton(self.TFrame, text = '16GB ($150)', variable = self.memoryVar,\
                value = 150, command = self.set_memory1)
        self.rb4 = tkinter.Radiobutton(self.TFrame, text = '32GB ($250)', variable = self.memoryVar,\
                value = 250, command = self.set_memory2)

        # Hard Drive Options
        self.hardDriveVar = tkinter.IntVar()
        self.rb5 = tkinter.Radiobutton(self.TFrame, text = '512GB ($100)', variable = self.hardDriveVar,\
                value = 100, command = self.set_hard_drive1)
        self.rb6 = tkinter.Radiobutton(self.TFrame, text = '1TB ($150)', variable = self.hardDriveVar,\
                value = 150, command = self.set_hard_drive2)
        self.rb7 = tkinter.Radiobutton(self.TFrame, text = '2TB ($225)', variable = self.hardDriveVar,\
                value = 225, command = self.set_hard_drive3)

        # Monitor Options
        self.monitorVar = tkinter.IntVar()
        self.rb8 = tkinter.Radiobutton(self.TFrame, text = '19" ($200)', variable = self.monitorVar,\
                value = 200, command = self.set_monitor1)
        self.rb9 = tkinter.Radiobutton(self.TFrame, text = '21" ($300)', variable = self.monitorVar,\
                value = 300, command = self.set_monitor2)
        self.rb10 = tkinter.Radiobutton(self.TFrame, text = '24" ($400)', variable = self.monitorVar,\
                value = 400, command = self.set_monitor3)

        # Okay and quit buttons
        self.okBtn = tkinter.Button(self.BFrame, text = 'OK', command=self.calculate_total)
        self.QuitBtn = tkinter.Button(self.BFrame, text = 'Quit', command=self.main_window.destroy)
        
        # Pack frames
        self.TFrame.pack()
        self.BFrame.pack()

        # Pack radio button options 
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()
        self.rb6.pack()
        self.rb7.pack()
        self.rb8.pack()
        self.rb9.pack()
        self.rb10.pack()
        
		# Pack ok and quit buttons
        self.okBtn.pack(side = 'left')
        self.QuitBtn.pack(side = 'left')
        
		# the main loop
        tkinter.mainloop()

    # Processor Methods
    def set_processor1(self):
        self.processorCost = 250

    def set_processor2(self):
        self.processorCost = 350

    # Memory Methods
    def set_memory1(self):
        self.memoryCost = 150

    def set_memory2(self):
        self.memoryCost = 250

    # Hard Drive Methods
    def set_hard_drive1(self):
        self.hardDriveCost = 100

    def set_hard_drive2(self):
        self.hardDriveCost = 150

    def set_hard_drive3(self):
        self.hardDriveCost = 225

    # Monitor Methods
    def set_monitor1(self):
        self.monitorCost = 200

    def set_monitor2(self):
        self.monitorCost = 300

    def set_monitor3(self):
        self.monitorCost = 400

    # Calculate Total
    def calculate_total(self):
        self.total = self.processorCost + self.memoryCost + self.hardDriveCost + self.monitorCost
        tkinter.messagebox.showinfo('Total Cost', f'The total cost is ${self.total}.')

my_gui = MyGUI()
