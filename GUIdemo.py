import tkinter

##class Donuts:
##    def __init__(self):
##        self.mainWindow = tkinter.Tk()
##
##        self.top_frame = tkinter.Frame(self.mainWindow)
##        self.bottom_frame = tkinter.Frame(self.mainWindow)
##
##        self.label = tkinter.Label(self.top_frame, text = "Types of People to Avoid:")
##        
##        self.label_1 = tkinter.Label(self.bottom_frame, text = "Mean")
##        self.label_2 = tkinter.Label(self.bottom_frame, text = "Angry")
##        self.label_3 = tkinter.Label(self.bottom_frame, text = "Coffee Addict")
##        
##        self.label.pack()
##        self.label_1.pack()
##        self.label_2.pack()
##        self.label_3.pack()
##
##        self.top_frame.pack()
##        self.bottom_frame.pack()
##        
##        tkinter.mainloop()

##donutDemo = Donuts()

import tkinter.messagebox

##class MyGUI:
##    def __init__(self):
##        self.mainWindow = tkinter.Tk()
##        self.my_button = tkinter.Button(self.mainWindow, text='Click Me!', command=self.do_something)
##        self.my_button.pack()
##        tkinter.mainloop()
##    def do_something(self):
##        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')
##
##my_gui = MyGUI()


class MyGUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()

        self.results = tkinter.StringVar()

        self.top_frame = tkinter.Frame(self.mainWindow)
        self.mid_frame = tkinter.Frame(self.mainWindow)
        self.bottom_frame = tkinter.Frame(self.mainWindow)

        self.label = tkinter.Label(self.top_frame, text='Enter a distance in kilometers:')
        self.entry = tkinter.Entry(self.top_frame, width=10)

        self.label.pack(side='left')
        self.entry.pack(side='left')
        self.top_frame.pack()

        self.outputLabel = tkinter.Label(self.mid_frame, text='Converted to miles: ')
        self.resultLabel = tkinter.Label(self.mid_frame, textvariable=self.results)
        self.outputLabel.pack(side='left')
        self.resultLabel.pack(side='left')
        self.mid_frame.pack()

        self.my_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.do_something)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.mainWindow.destroy)
        
        self.my_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def do_something(self):
        kilo = float(self.entry.get())
        miles = kilo * 0.6214
        self.results.set(miles)
##        tkinter.messagebox.showinfo('Results', str(kilo) + ' kilometers is equal to ' + str(miles) +'miles.')

myButton = MyGUI()    



##what is tkinter - GUI module that allows python to create simple GUI programs
## callback function = executes when user clicks the button
##                     A.K.A. event handler - handles even that occurs when the user clicks the button
##syntax for frame
##how many widgets are there - 15 widgets
