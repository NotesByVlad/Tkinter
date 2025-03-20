### Toolbar (Custom Using Frame) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("Toolbar Example")  # Set the window title

# Create a Frame for the toolbar
toolbar = tk.Frame(root, bg="gray")

# Create buttons inside the toolbar
button1 = tk.Button(toolbar, text="New", padx=5, pady=2)
button2 = tk.Button(toolbar, text="Open", padx=5, pady=2)

# Pack the buttons inside the toolbar
button1.pack(side="left", padx=2, pady=2)
button2.pack(side="left", padx=2, pady=2)

# Pack the toolbar at the top of the window
toolbar.pack(side="top", fill="x")

root.mainloop()  # Start the Tkinter event loop