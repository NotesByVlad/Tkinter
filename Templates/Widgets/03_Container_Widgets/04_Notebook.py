### Notebook (Tabbed Interface) ###

import tkinter as tk  # Import Tkinter
from tkinter import ttk  # Import themed widgets

# Create the main application window
root = tk.Tk()
root.title("Notebook Example")  # Set the window title

# Create a Notebook widget (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)  # Expand to fit the window

# Create two frames (tabs)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

# Add tabs to the Notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Add content to the tabs
label1 = tk.Label(tab1, text="This is Tab 1")  # Create a label
label1.pack(pady=10)  # Pack the label into Tab 1

label2 = tk.Label(tab2, text="This is Tab 2")  # Create a label
label2.pack(pady=10)  # Pack the label into Tab 2

root.mainloop()  # Start the Tkinter event loop