# exKilo_conv1.py

import tkinter
import tkinter.messagebox

class KiloGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.TFrame = tkinter.Frame(self.main_window)
        self.BFrame = tkinter.Frame(self.main_window)

        self.PLabel = tkinter.Label(self.TFrame, text = "Enter a distance in km: ")
        self.entry = tkinter.Entry(self.TFrame, width = 10)

        self.calcBtn = tkinter.Button(self.BFrame, text = "Convert", command = self.convert)

        self.QuitBtn = tkinter.Button(self.BFrame, text = "Quit", command = self.main_window.destroy)

        self.PLabel.pack(side = 'left')
        self.entry.pack(side = 'left')
        self.calcBtn.pack(side = 'left')
        self.QuitBtn.pack(side = 'left')
        self.TFrame.pack()
        self.BFrame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.entry.get())
        miles = kilo * 0.6124

        tkinter.messagebox.showinfo('Result', f'{kilo:.3f} km is equal to {miles:.3f}')

KiloObj = KiloGUI()


