import tkinter as tk
from tkinter import simpledialog
from simulation_window import Simulation

def ask_disease_name():
    root = tk.Tk()
    root.withdraw()

    disease = simpledialog.askstring(
        "Nazwa choroby",
        "Podaj nazwę choroby:"
    )

    root.destroy()
    return disease

if __name__ == '__main__':
    name = ask_disease_name()
    if not name:
        print('see ya later alligator')
    else:
        root = tk.Tk()
        s = Simulation(root, name)
        root.mainloop()