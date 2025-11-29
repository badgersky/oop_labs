import tkinter as tk

W = 1000
H = 1000

class Simulation:

    def __init__(self, root):
        self.root = root
        self.root.title("Symulacja choroby bardzo groźnej")
        self.canvas = tk.Canvas(root, width=W, height=H, bg="white")
        self.canvas.pack()