# src/main.py
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter App")
        self.root.geometry("400x300")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Widgets
        self.label = ttk.Label(main_frame, text="Welcome to My App!")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.entry = ttk.Entry(main_frame, width=30)
        self.entry.grid(row=1, column=0, columnspan=2, pady=5)
        
        self.button = ttk.Button(main_frame, text="Click Me!", command=self.on_button_click)
        self.button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
    
    def on_button_click(self):
        text = self.entry.get()
        if text:
            messagebox.showinfo("Hello", f"You entered: {text}")
        else:
            messagebox.showwarning("Warning", "Please enter some text!")

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()