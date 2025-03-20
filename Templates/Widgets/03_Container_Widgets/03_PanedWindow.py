### PanedWindow (Resizable Sections) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("PanedWindow Example")  # Set the window title

# Create a PanedWindow (split window)
paned_window = tk.PanedWindow(root, orient="horizontal")  # Set orientation to horizontal
paned_window.pack(fill="both", expand=True)  # Expand it fully

# Add two frames inside the PanedWindow
left_frame = tk.Frame(paned_window, bg="lightblue", width=100, height=200)
right_frame = tk.Frame(paned_window, bg="lightgreen", width=100, height=200)

paned_window.add(left_frame)  # Add left frame
paned_window.add(right_frame)  # Add right frame

root.mainloop()  # Start the Tkinter event loop