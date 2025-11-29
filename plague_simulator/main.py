import tkinter as tk
from simulation_window import Simulation

if __name__ == '__main__':
    root = tk.Tk()
    s = Simulation(root)
    root.mainloop()