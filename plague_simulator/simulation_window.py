import tkinter as tk

W = 1000
H = 1000

class Simulation:

    def __init__(self, root, name='katar'):
        self.root = root
        self.root.title(name)
        self.canvas = tk.Canvas(root, width=W, height=H, bg='white')
        self.canvas.pack()