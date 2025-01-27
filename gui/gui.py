import tkinter as tk
from tkinter import messagebox

class PenTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Penetration Testing Framework")

        tk.Label(root, text="PenTest Framework", font=("Arial", 16)).pack(pady=10)

        tk.Button(root, text="Run OSINT", command=self.run_osint).pack(pady=5)
        tk.Button(root, text="Run Scanning", command=self.run_scanning).pack(pady=5)
        tk.Button(root, text="Run Brute Force", command=self.run_brute_force).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def run_osint(self):
        messagebox.showinfo("OSINT", "OSINT module executed.")

    def run_scanning(self):
        messagebox.showinfo("Scanning", "Scanning module executed.")

    def run_brute_force(self):
        messagebox.showinfo("Brute Force", "Brute force module executed.")