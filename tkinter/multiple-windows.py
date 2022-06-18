import tkinter as tk

HEIGHT = 250
WIDTH = 250


def newWindow():
    window = tk.Toplevel()
    window.title("New Window")
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    canvas.pack()


ws = tk.Tk()
ws.title("Main Window")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(ws, text="New Window", bg='White',
                   fg='Black', command=lambda: newWindow())

button.pack()
ws.mainloop()
