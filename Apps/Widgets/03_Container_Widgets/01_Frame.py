### Frame (Container for Widgets) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("Frame Example")  # Set the window title

# Create a Frame (a container for other widgets)
frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)  # Set background color and padding
frame.pack(padx=20, pady=20)  # Pack the frame into the window

# Add widgets inside the frame
label = tk.Label(frame, text="Hello from Frame!")  # Create a label
label.pack(pady=5)  # Pack the label into the frame

root.mainloop()  # Start the Tkinter event loop