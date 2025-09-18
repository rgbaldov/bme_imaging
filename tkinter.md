# Tkinter Lecture Notes

## Introduction
**Tkinter** is the standard Python library for creating **Graphical User Interfaces (GUIs)**. It provides tools to build windows, buttons, labels, text boxes, menus, and more.
- Built-in Python library (no need to install separately in most cases).  
- Cross-platform (works on Windows, macOS, Linux).  
- Lightweight and simple to learn.  

## Creating Your First Tkinter Window:
```python
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the application
root.mainloop()
