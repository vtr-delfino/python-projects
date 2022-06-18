from tkinter import *
from tkinter import ttk


class feetToMeters:

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass

    def __init__(self, root):

        # Set the main application title
        root.title("Testando GUI no Python")

        # Set a Content Frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Set the Entry Widget
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(
            column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(
            column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equal to").grid(
            column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        feet_entry.focus()
        root.bind("<Return>", self.calculate)


class calculator:

    def __init__(self, root):

        root.title("Calculadora")

        mainframe = ttk.Frame(root, padding="5 5 5 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.number = StringVar()
        feet_entry = ttk.Entry(mainframe, width=10, textvariable=self.number)
        feet_entry.grid(column=1, row=1, sticky=(W, E))

        ttk.Button(mainframe, text="Enter", command="").grid(
            column=2, row=1, sticky=E)

        #Buttons (try clean)
        ttk.Button(mainframe, text="7", command="").grid(
            column=1, row=2, sticky=W)

        ttk.Button(mainframe, text="8", command="").grid(
            column=2, row=2, sticky=W)
        
        ttk.Button(mainframe, text="9", command="").grid(
            column=3, row=2, sticky=W)
        
        ttk.Button(mainframe, text="4", command="").grid(
            column=1, row=3, sticky=W)
        
        ttk.Button(mainframe, text="5", command="").grid(
            column=2, row=3, sticky=W)
        
        ttk.Button(mainframe, text="6", command="").grid(
            column=3, row=3, sticky=W)
        
        ttk.Button(mainframe, text="1", command="").grid(
            column=1, row=4, sticky=W)
        
        ttk.Button(mainframe, text="2", command="").grid(
            column=2, row=4, sticky=W)
        
        ttk.Button(mainframe, text="3", command="").grid(
            column=3, row=4, sticky=W)


# Set the main application Window
root = Tk()
calculator(root)
root.mainloop()
