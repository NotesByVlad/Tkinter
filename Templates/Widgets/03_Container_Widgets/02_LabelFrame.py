### LabelFrame (Titled Container) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("LabelFrame Example")  # Set the window title

# Create a LabelFrame with a title
labelframe = tk.LabelFrame(root, text="Options", padx=10, pady=10)
labelframe.pack(padx=20, pady=20)  # Pack the LabelFrame into the window

# Add widgets inside the LabelFrame
button1 = tk.Button(labelframe, text="Button 1")  # Create a button
button2 = tk.Button(labelframe, text="Button 2")  # Create another button
button1.pack(pady=5)  # Pack button 1 into the LabelFrame
button2.pack(pady=5)  # Pack button 2 into the LabelFrame

root.mainloop()  # Start the Tkinter event loop